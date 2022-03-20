import requests
import json
import login

api_key=login.nytAPI
year=input('year --')
month=input('month --')
base_api_url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={api_key}'

r=requests.get(base_api_url)
archiveData=r.json()
with open('nyt-archive-'+year+month+'.json','w') as jsonDatabase:
    json.dump(archiveData, jsonDatabase)
    
#======json.dump writes to a file or file-like object, whereas json.dumps returns a string==========#
print('total hits from month', month, 'and year',year,' on NYT-archive are ',archiveData['response']['meta']['hits'])
# store this data or extract your project required info and dtore it into database
# as always reading API docs is the best way to go about APIs
# note: data sould be very large depending on 