USERNAME = "iangago"
import github.github_api as gtapi
import readme as readme
import storage.files as files

repos = gtapi.get_repositories(USERNAME)
repos = gtapi.filter_repos(repos)

ac = gtapi.get_activity(USERNAME)
ac = gtapi.filter_activity(ac)

files.update_all(readme.create_readme_projects(repos), readme.create_readme_git_status(repos), readme.create_readme_activity(ac))




