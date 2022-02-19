'''
This is my own implementation of the project available on:
https://realpython.com/build-a-python-weather-app-cli/

login.py file stores my api key.
TODO: use secrets.ini type file for next automation project.
TODO: 
'''

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
        # print(r.json())
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
            searchList=[(city['EnglishName']+'-'+city['AdministrativeArea']['LocalizedName']+'-'+city['Key']) for city in searchResults[:5]] # only shows top 5 results
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
    print(r.json())
    try:
        limitData=r.headers['RateLimit-Remaining']
        print('remainig quota of the day >>> ',limitData)
    except:
        pass
    return r.json()

def formatter(lstr,rstr):
    strLen=60
    print(lstr.ljust(strLen-len(lstr)-len(rstr),'=')+rstr)

try:
    currentData=currentConditions(locationKey)[0]
    tempM=str(currentData['Temperature']['Metric']['Value'])+' C'
    tempI=str(currentData['Temperature']['Imperial']['Value'])+' F'
    if currentData['IsDayTime']:
        daynight='Day'
    else:
        daynight='Night'
    print('Weather Info'.center(40,'='))
    formatter('Location ',query.upper())
    formatter('Weather Type ',currentData['WeatherText'])
    formatter('Day or Night ',daynight)
    formatter('Metric Temp ',tempM)
    formatter('Imperial Temp ',tempI)
    # print('Location'.ljust(strLen-len()-len(),'.')+(query.upper()).rjust())
    # print('Weather Type'.ljust(strLen-len()-len(),'.')+(currentData['WeatherText']).rjust())
    # print('Day or Night'.ljust(strLen-len()-len(),'.')+(daynight).rjust())
    # print('Metric Temp'.ljust(strLen-len()-len(),'.')+(str(tempM)+' C').rjust())
    # print('Imperial Temp'.ljust(strLen-len()-len(),'.')+(str(tempI)+' F').rjust())
    print('Have a Great Day'.center(40,'='))
except:
    print('No weather info available.')