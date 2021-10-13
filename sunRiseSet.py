import requests
from datetime import datetime
import login
# from prompt_toolkit import prompt
from PyInquirer import prompt

apiKey=login.battutaAPI
today=str(datetime.now())[1:10]


def battutaQuota(apiKey):
    URL=f'http://battuta.medunes.net/api/quota/?key={apiKey}'
    quotaLeft=requests.get(URL).json()[0]
    print('Remaining quota count on battuta',quotaLeft['remaining quota'])
    return

def getCountryCode(apiKey):
    URL=f'http://battuta.medunes.net/api/country/all/?key={apiKey}'
    codeJSON=requests.get(URL).json()
    return codeJSON

'''
return: list of dict with keys: name and code
codes: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
response:
[{"name":"COUNTRY_NAME_1","code":"COUNTRY_CODE_1"},{"name":"COUNTRY_NAME_2","code":"COUNTRY_CODE_2"},..]
'''

'''
def getCity(country,region,apiKey):
    url=f'http://battuta.medunes.net/api/city/search/?region={region}&city={city}&key={apiKey}'
    hintData=requests.get(url).json()
    return hintData
'''
country=input('country --')
'''
these also can be specified but will work with country only here
region=input('region --')
city=input('city --')
'''

def getCountry(country,apiKey):
    url=f'http://battuta.medunes.net/api/country/search/?country={country}&key={apiKey}'
    countryList=requests.get(url).json()
    print(countryList)
    return countryList

countryHint=getCountry(country,apiKey)
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
    print(answer['type'])
    return answer

answer=prompter(countryHint)
countryName=answer['type']
for country in countryHint:
    if countryName in country.values():
        countrySelected=country['code']
        print(countrySelected,'---- country ISO code')
        break

def getRefions(countrySelected,apiKey):
    url=f'http://battuta.medunes.net/api/region/{countrySelected}/all/?key={apiKey}'
    regionList=requests.get(url).json()
    print(regionList)
    return regionList

regionHint=getRefions(countrySelected,apiKey)

regionList=[region['region'] for region in regionHint]
whichRegion=[
        {
            'type':'list',
            'name':'type',
            'message':'please choose a option:',
            'choices':regionList,
            'default':0
        }
    ]
answer=prompt(whichRegion)
regionSelected=answer['type']
print(regionSelected,'---- region in ',countryName)

citySelected=input('city hint in the region -- ')
'''
# it does not seems to work
def getCity(regionSelected,apiKey):
    url=f'http://battuta.medunes.net/api/city/fr/search/?region={regionSelected}&key={apiKey}'
    cityList=requests.get(url).json()
    return cityList

city=getCity(regionSelected,apiKey)

answer=prompter(city)
citySelected=answer['type']['city']
print(citySelected,'----city')
'''
# somehow API is not rsponding
'''
def getLanLet(regionSelected,citySelected,apiKey):
    url=f'http://battuta.medunes.net/api/city/search/?region={regionSelected}&city={citySelected}&key={apiKey}'
    latlanData=requests.get(url)
    print(latlanData.status_code)
    print(latlanData.json())
    return latlanData.json()

latlanData=getLanLet(regionSelected,citySelected,apiKey)

cityList=[city['city'] for city in latlanData]
whichCity=[
        {
            'type':'list',
            'name':'type',
            'message':'please choose a option:',
            'choices':cityList,
            'default':0
        }
    ]
answer=prompt(whichCity)
cityName=answer['type']
print(cityName,'---- region in ',countryName)

for city in cityList:
    if cityName in city.values():
        latlanData={'lat':latlanData['latitude'],'lan':latlanData['longitude']}
        break
    else:
        print('na-valid latlanData available for regiona and city')
'''
latlanData={'lat':'36.7201600','lan':'-4.4203400'}
def getRiseSet(lat,lng,date=today): #<-- date format = '2021-10-13'
    URL=f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}'
    data=requests.get(URL).json()
    print(data['status'],' --- status')
    return data['results']
if latlanData!=None:
    data=getRiseSet(latlanData['lat'],latlanData['lan'])
    print('Sunrise at -- ',data['sunrise'])
    print('Sunset at -- ',data['sunset'])
    print("Don't have a good day. Have a great day!")
else:
    print('No data available. try again.')

battutaQuota(apiKey)