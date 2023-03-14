import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Make API call and store the response 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept': 'application/vnd.github.v3+json'}
r= requests.get(url, headers=headers)
print(f"Status code {r.status_code}")

#Store API RESPONSE IN A DICTIONARY 
response_dict= r.json()

#Process results
# print(response_dict.keys())
# print(f"Total repositories: {response_dict['total_count']}")

# #Explore info about the repos
repos_dict= response_dict['items']
# print(f"Repositories returned: {len(repos_dict)}")
#Examine the 1st repo
# repo_dict=repos_dict[0]
# print(f"\n keys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

repo_names=[]
stars=[]
labels=[]

#Selected info about the first repo
print("Info about the 1st repo")
for repo_dict in repos_dict:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    owner= repo_dict['owner']['login']
    description= repo_dict['description']
    label= f"{owner} <br /> {description}"
    labels.append(label)

data=[{'type': 'bar',
       'x':repo_names,
       'y':stars,
       'hovertext':labels,
       'marker':{'color':'rgb(60,100,150)',
                 'line':{'width':1.5, 'color':'rgb(25,25,25)'},
                 },
        'opacity':0.6}]

my_layout={'title':'Most stared python project on github.',
           'xaxis':{'title':'repository'},
           'yaxis':{'title':'stars'},
           }

fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='python_repos.html')
