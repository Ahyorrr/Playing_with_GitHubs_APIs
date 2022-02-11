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

# examining first repository
repo_dict = repo_dicts[0]
print(f"\nKey: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print(f"Name: {repo_dict['name']}")
