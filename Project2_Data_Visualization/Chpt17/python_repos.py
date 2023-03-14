import requests

#Make API call and store the response 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept': 'application/vnd.github.v3+json'}
r= requests.get(url, headers=headers)
print(f"Status code {r.status_code}")

#Store API RESPONSE IN A DICTIONARY 
response_dict= r.json()

#Process results
# print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

#Explore info about the repos
repos_dict= response_dict['items']
print(f"Repositories returned: {len(repos_dict)}")

#Examine the 1st repo
repo_dict=repos_dict[0]
print(f"\n keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

#Selected info about the first repo
print("Info about the 1st repo")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")