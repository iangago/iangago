def rank_repos_stars(repositories):
    repositories.sort(key=lambda x: x["stars"], reverse=True)

    return repositories

def top_three_projects(sorted_repositories):
    return sorted_repositories[:3]
