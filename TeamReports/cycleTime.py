import requests
import json
import csv
from datetime import datetime

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

# Calculate PR cycle times
def calculate_pr_cycle_times(pr_data):
    cycle_times = []
    for pr in pr_data:
        created_at = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        closed_at = datetime.strptime(pr["closed_at"], "%Y-%m-%dT%H:%M:%SZ") if pr["closed_at"] else None
        if closed_at:
            cycle_time = (closed_at - created_at).total_seconds() / 3600  # Convert to hours
            cycle_times.append({
                "author": pr["user"]["login"],
                "cycle_time_hours": cycle_time
            })
    return cycle_times

# Paginate through all PRs
def get_all_pull_requests():
    page = 1
    all_prs = []
    while True:
        prs = fetch_pull_requests(page=page)
        if not prs:
            break
        all_prs.extend(prs)
        page += 1
    return all_prs

# Main
all_prs = get_all_pull_requests()
pr_cycle_times = calculate_pr_cycle_times(all_prs)

# Group by author
from collections import defaultdict
author_cycle_times = defaultdict(list)
for entry in pr_cycle_times:
    author_cycle_times[entry["author"]].append(entry["cycle_time_hours"])

# Calculate average cycle time per author
author_avg_cycle_time = {author: sum(times)/len(times) for author, times in author_cycle_times.items()}

# Print results
print(json.dumps(author_avg_cycle_time, indent=4))


# Save results to CSV
with open('pr_cycle_times.csv', 'w', newline='') as csvfile:
    fieldnames = ['author', 'average_cycle_time_hours']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for author, avg_cycle_time in author_avg_cycle_time.items():
        writer.writerow({'author': author, 'average_cycle_time_hours': avg_cycle_time})
