import filter.ranking as ranking
USERNAME = "iangago"
import filter.data_refining as datar

def create_readme_projects(repos):
    repos = ranking.top_three_projects(repos)

    readme_section_projects = "## Featured Projects\n"

    i = 1
    for repo in repos:
        readme_section_projects += f"\n\n### {i}. {repo['name']}\n"
        if repo['description'] == None:
            readme_section_projects += f"    No description found."
        else:
            readme_section_projects += f"    {repo['description']}"
        readme_section_projects += f"\n    Stars: {repo['stars']} | {repo['language']}"
        i += 1

    return readme_section_projects

def create_readme_git_status(repos):
    total_repos = datar.get_total_repos(repos)

    total_stars = datar.get_total_stars(repos)
    
    main_language = datar.most_used_language(repos)

    readme_section_status = "## GitHub Stats\n\n"

    readme_section_status += f"### - Total Projects: {total_repos}\n"
    readme_section_status += f"### - Total Stars: {total_stars}\n"
    readme_section_status += f"### - Avg Stars per Project: {total_stars / total_repos:.1f}\n"

    if main_language == None or len(main_language) < 2:
        readme_section_status += "### - Laguages Used: Not Found\n"
    else:
        readme_section_status += f"### - Laguages Used:\n"
        i = 1
        top_count = 0
        for language in main_language[1:]:
            if i < 4:
                top_count += (language[1] / main_language[0])
                readme_section_status += f"- {language[0]} ({(language[1] / main_language[0]) * 100:.1f}%)\n"
            else:
                readme_section_status += f"- Others ({100 - (top_count * 100):.1f}%)\n"
                break
            i += 1

    return readme_section_status

def create_readme_activity(activity):
    readme_section_status = "## Recent Activity\n\n"

    readme_section_status += f"### - Pushes: {activity[1]['total_pushes']}\n"
    readme_section_status += f"### - Active Repositories: {len(activity[0])}\n"
    try:
        readme_section_status += f"### - Most Active Project: {list(activity[0])[0][len(USERNAME) + 1:]}\n"
    except IndexError: 
        readme_section_status += f"### - Most Active Project: No active project.\n" 
        
    return readme_section_status


