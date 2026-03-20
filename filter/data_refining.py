def get_total_repos(repos_list):
    return len(repos_list)

def get_total_stars(repos_list):
    star_count = 0

    for repo in repos_list:
        star_count += repo['stars']

    return star_count

def most_used_language(repos_list):
    language_count = {}
    total_count = 0

    for repo in repos_list:
        lang = repo["language"]
        
        if lang is None:
            continue

        if lang in language_count:
            language_count[lang] += 1
        else:
            language_count[lang] = 1
            
        total_count += 1

    sorted_language = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

    sorted_language.insert(0, total_count)

    return sorted_language