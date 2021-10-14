import login
import requests
from PyInquirer import prompt

openAPI=login.openAPI

def geoLocator(city,apikey=openAPI,limit=5):
    url=f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={apikey}'
    try:
        r=requests.get(url)

        print('total search results by geolocation >>>',len(r.json()))

        return r.json()
    except:
        print('something went wrong in geoLocator')

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

# print('search query >>> ')
city=input('search query city name >>> ')
'''stateCode=input('state code >>> ')
countryCode=input('country code >>> ')'''

if city == '':
    city='sujangarh'
    print('There was no search query. Default city is >>> ',city)
searchResults=geoLocator(city)
if len(searchResults)>0:
    '''
    to handle cases like not valid api and what not
    '''
    try:
        searchList=[(city['name']+'&'+city.get('state','noState')+'&'+city.get('country','noCountry')+'&'+str(city['lat'])+'&'+str(city['lon'])) for city in searchResults]
        answer=prompter(searchList)
        latlanData=answer['type'].split('&')
        lat=latlanData[-2]
        lon=latlanData[-1]
        #print(latlanData)
    except Exception as e:
        print(e)
else:
    print('try with a valid query. exiting now.')
    exit()

def airPoll(lat,lon,apikey=openAPI):
    url=f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apikey}'
    try:
        r=requests.get(url)
        return r.json()
    except:
        print('something went wrong in airpollution')

try:
    airData=airPoll(lat,lon)['list'][0]
    aqi=str(airData['main']['aqi'])
    components=airData['components']
    aqiDict={
        '1':'Good',
        '2':'Fair',
        '3':'Moderate',
        '4':'Poor',
        '5':'Very poor'
    }
    print('Pollution Info'.center(40,'='))
    print('Location'.ljust(20,'.')+(city.upper()).rjust(20))
    print('AQI Value'.ljust(25,'.')+(aqiDict[aqi]).rjust(15))
    print('Carbon monoxide'.ljust(30,'.')+str(components.get('co',-1)).rjust(10))
    print('Nitrogen monoxide'.ljust(30,'.')+str(components.get('no',-1)).rjust(10))
    print('Nitrogen dioxide'.ljust(30,'.')+str(components.get('no2',-1)).rjust(10))
    print('Sulphur dioxide'.ljust(30,'.')+str(components.get('so2',-1)).rjust(10))
    print('Have a Great Day'.center(40,'='))
except:
    print('No weather info available.')