def update_readme_projects(generated_text):
    #set markers
    start_marker_projects = "<!-- START:PROJECTS -->"
    end_marker_projects = "<!-- END:PROJECTS -->"

    #open and read readme as a string
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    #track the index of the beggining and the end of the markers
    start_index = content.find(start_marker_projects)
    end_index = content.find(end_marker_projects)

    #check errors
    if start_index == -1 or end_index == -1:
        print("Markers not found")
        exit()

    #store before as everyting
    before = content[:start_index + len(start_marker_projects)]
    after = content[end_index:]

    #sets new content of the readme
    new_content = (
        before
        + "\n\n"
        + generated_text
        + "\n\n"
        + after
    )

    #rewrites file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

def update_readme_stats(generated_text):
    #set markers
    start_marker_stats = "<!-- START:STATS -->"
    end_marker_stats = "<!-- END:STATS -->"

    #open and read readme as a string
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    #track the index of the beggining and the end of the markers
    start_index = content.find(start_marker_stats)
    end_index = content.find(end_marker_stats)

    #check errors
    if start_index == -1 or end_index == -1:
        print("Markers not found")
        exit()

    #store before as everyting
    before = content[:start_index + len(start_marker_stats)]
    after = content[end_index:]

    #sets new content of the readme
    new_content = (
        before
        + "\n\n"
        + generated_text
        + "\n\n"
        + after
    )

    #rewrites file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

def update_readme_activity(generated_text):
    #set markers
    start_marker_ac = "<!-- START:ACTIVITY -->"
    end_marker_ac = "<!-- END:ACTIVITY -->"

    #open and read readme as a string
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    #track the index of the beggining and the end of the markers
    start_index = content.find(start_marker_ac)
    end_index = content.find(end_marker_ac)

    #check errors
    if start_index == -1 or end_index == -1:
        print("Markers not found")
        exit()

    #store before as everyting
    before = content[:start_index + len(start_marker_ac)]
    after = content[end_index:]

    #sets new content of the readme
    new_content = (
        before
        + "\n\n"
        + generated_text
        + "\n\n"
        + after
    )

    #rewrites file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

def update_all(project_text, stats_text, activity_text):
    update_readme_projects(project_text)
    update_readme_stats(stats_text)
    update_readme_activity(activity_text)