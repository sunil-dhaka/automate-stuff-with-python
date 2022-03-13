from sympy import im
import login,requests,json
from bs4 import BeautifulSoup as bs
from twilio.rest import Client

from twilioSMS import twilioSMS

def getRainAlert(lat='37.69109000000003',lon='-122.47278999999997'):
    '''
    Input:
        lat\\
        lon
    
    lat and lon can be changed for different location
    '''
    url=f'https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}'
    r=requests.get(url)
    soup=bs(r.text,'html.parser')
    forecast_text=soup.find_all('li',class_='forecast-tombstone')[0].text
    if 'rain' in forecast_text:
        alert_message='Likely to rain.'
    else:
        alert_message='NOT likely to rain.'
    return alert_message

twilioSMS(getRainAlert())