import requests
import filter.ranking as ranking

def get_repositories(username):
    page = 1
    all_repos = []

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url)
        data = response.json()
        
        if not data:
            break

        all_repos.extend(data)
        page += 1

    return all_repos

def get_activity(username):

    url = f'https://api.github.com/users/{username}/events'

    response = requests.get(url)

    activity = response.json()

    return activity

def filter_activity(activity):
    total_pushes = 0
    repo_activity = {}

    for event in activity:
        if event['type'] == 'PushEvent':
            total_pushes += 1

            repo_name = event["repo"]["name"]

            if repo_name not in repo_activity:
                repo_activity[repo_name] = 0

            repo_activity[repo_name] += 1
    
    return [repo_activity, {'total_pushes': total_pushes}]

def filter_repos(repos_data):
    clean_repos = []

    for repo in repos_data:   
        if (
            not repo["fork"] and
            not repo["archived"] and
            repo["size"] > 0
        ):
            clean_repos.append({
                'name': repo['name'],
                "stars": repo["stargazers_count"],
                "language": repo["language"],
                "description": repo["description"]
            })

    clean_repos = ranking.rank_repos_stars(clean_repos)

    return clean_repos

