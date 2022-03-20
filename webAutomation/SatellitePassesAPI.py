import requests

# to get lat and lan can use battuta but it seems to not work
url='https://satellites.fly.dev/passes/25544?lat=60&lon=-60&limit=1'

headers={'User-Agent': 'HTTPie/1.0.3'}

data=requests.get(url,headers=headers)

print(data.json())