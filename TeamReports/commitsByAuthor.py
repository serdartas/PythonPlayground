import requests
# Configuration
GITHUB_API_URL = "https://api.github.com"
ORG = "your_organization"
REPO = "your_repository"
TOKEN = "your_github_token"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch commits
def fetch_commits(page=1, per_page=100):
    url = f"{GITHUB_API_URL}/repos/{ORG}/{REPO}/commits"
    params = {
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Aggregate commits by author
def get_commits_per_developer():
    commit_page = 1
    commits_by_author = {}
    while True:
        commits = fetch_commits(page=commit_page)
        if not commits:
            break
        for commit in commits:
            author = commit['commit']['author']['name']
            if author not in commits_by_author:
                commits_by_author[author] = 0
            commits_by_author[author] += 1
        commit_page += 1
    return commits_by_author

commits_per_developer = get_commits_per_developer()
print(commits_per_developer)
