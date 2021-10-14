import login
import requests
from PyInquirer import prompt
import time

openAPI=login.openAPI

def timeConverter(epochTime):
    # for other locations also gives time acc to your localtime
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))

def getWeather(city,lang='en',apikey=openAPI,units='metric'):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}'
    r=requests.get(url)
    print(r.json())
    return r.json()

city=input('city name >>> ')
weatherData=getWeather(city,lang='hi')

if weatherData.get('message','noMessage')=='city not found':
    print('Sorry. ',weatherData['message'],'. Try again :| .')
    exit()
else:
    print('Weather(metric) Info'.center(50,'='))
    print('Location'.ljust(25,'.')+(city.upper()+' - '+weatherData['sys']['country']).rjust(25))
    # weather=weatherData['weather'][0]
    print('Weather main'.ljust(25,'.')+weatherData['weather'][0]['main'].rjust(25))
    print('Description'.ljust(25,'.')+weatherData['weather'][0]['description'].rjust(25))
    print('Temp Curr'.ljust(25,'.')+str(weatherData['main']['temp']).rjust(25))
    print('Temp Feels Like'.ljust(25,'.')+str(weatherData['main']['feels_like']).rjust(25))
    print('Temp Min'.ljust(25,'.')+str(weatherData['main']['temp_min']).rjust(25))
    print('Temp Max'.ljust(25,'.')+str(weatherData['main']['temp_max']).rjust(25))
    print('Wind Speed'.ljust(25,'.')+str(weatherData['wind']['speed']).rjust(25))
    print('Sunrise'.ljust(25,'.')+timeConverter(weatherData['sys']['sunrise']).rjust(25))
    print('Sunset'.ljust(25,'.')+timeConverter(weatherData['sys']['sunset']).rjust(25))
    print('Local Time'.ljust(25,'.')+timeConverter(weatherData['dt']).rjust(25))
    print('Have a Great Day'.center(50,'='))