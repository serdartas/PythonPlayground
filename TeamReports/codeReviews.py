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

# Fetch pull requests
def fetch_pull_requests(page=1, per_page=100):
    url = f"{GITHUB_API_URL}/repos/{ORG}/{REPO}/pulls"
    params = {
        "state": "all",
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Fetch reviews for a pull request
def fetch_reviews(pr_number):
    url = f"{GITHUB_API_URL}/repos/{ORG}/{REPO}/pulls/{pr_number}/reviews"
    response = requests.get(url, headers=headers)
    return response.json()

# Aggregate reviews by reviewer
def get_code_reviews():
    pr_page = 1
    reviewers = {}
    while True:
        prs = fetch_pull_requests(page=pr_page)
        if not prs:
            break
        for pr in prs:
            reviews = fetch_reviews(pr['number'])
            for review in reviews:
                reviewer = review['user']['login']
                if reviewer not in reviewers:
                    reviewers[reviewer] = 0
                reviewers[reviewer] += 1
        pr_page += 1
    return reviewers

code_reviews = get_code_reviews()
print(code_reviews)
