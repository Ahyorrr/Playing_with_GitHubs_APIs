import requests

# making API call and storing response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
header = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=header)
print(f"Status code: {r.status_code}")

# storing API response
response_dict = r.json()

# processing results
print(response_dict.keys())
print(f"Total Repositories: {response_dict['total_count']}")

# examining all repositories
repo_dicts = response_dict['items']
print(f"Returned repositories: {len(repo_dicts)}")

# examining info on top repositories
print('\nSelected information about each repository')
for repo_dict in repo_dicts:
    print('\n')
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
