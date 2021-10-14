import login
import requests
from PyInquirer import prompt

accuAPI=login.accuAPI
'''
need to make a login.py file with accuAPI variable being your apikey
also in the same folder
'''
def searchText(query,apiKey=accuAPI):
    url='http://dataservice.accuweather.com/locations/v1/search?q='+ '+'.join(query.split(' '))+f'&apikey={apiKey}'
    try:
        r=requests.get(url)
        #print(r.json())
        print('total results for search query are >>> ',len(r.json()))
        return r.json()
    except:
        print('something went wrong')
def prompter(promptList):
    whichCountry=[
            {
                'type':'list',
                'name':'type',
                'message':'please choose a option:',
                'choices':promptList,
                'default':0
            }
        ]
    answer=prompt(whichCountry)
    #print(answer['type'])
    return answer

query=input('search query >>> ')
if query=='':
    locationKey='200328'
else:
    searchResults=searchText(query)
    if len(searchResults)>0:
        '''
        to handle cases like not valid api and what not
        '''
        try:
            searchList=[(city['EnglishName']+'-'+city['AdministrativeArea']['LocalizedName']+'-'+city['Key']) for city in searchResults]
            answer=prompter(searchList)
            locationKey=answer['type'].split('-')[-1]
            #print(locationKey)
        except Exception as e:
            print(e)
    else:
        print('try with a valid query. exiting now.')
        exit()

def currentConditions(locationKey,apiKey=accuAPI):
    url=f'http://dataservice.accuweather.com/currentconditions/v1/{locationKey}?&apikey={apiKey}'

    r=requests.get(url)
    #print(r.json())
    try:
        limitData=r.headers['RateLimit-Remaining']
        print('remainig quota of the day >>> ',limitData)
    except:
        pass
    return r.json()
try:
    currentData=currentConditions(locationKey)[0]
    tempM=currentData['Temperature']['Metric']['Value']
    tempI=currentData['Temperature']['Imperial']['Value']
    if currentData['IsDayTime']:
        daynight='Day'
    else:
        daynight='Night'
    print('Weather Info'.center(40,'='))
    print('Location'.ljust(20,'.')+(query.upper()).rjust(20))
    print('Weather Type'.ljust(25,'.')+(currentData['WeatherText']).rjust(15))
    print('Day or Night'.ljust(30,'.')+(daynight).rjust(10))
    print('Metric Temp'.ljust(30,'.')+(str(tempM)+' C').rjust(10))
    print('Imperial Temp'.ljust(30,'.')+(str(tempI)+' F').rjust(10))
    print('Have a Great Day'.center(40,'='))
except:
    print('No weather info available.')