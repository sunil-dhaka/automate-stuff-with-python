import webbrowser
import requests
import json
import PyInquirer
import time
from PyInquirer import prompt

status_green=False
while(status_green==False):
    # input
    key=input('Please paste your api key:')
    query=input("Which city's weather info do you want to get:")
    r=requests.get('https://dataservice.accuweather.com/locations/v1/cities/search',params={
        'apikey':key,
        'q':query
    })

    if r.status_code==200:
        print('We are good to go.')
        status_green=True
    else:
        print('please re-enter your api key and query location.')
        time.sleep(0.5)

data_obtained=r.json()
if len(data_obtained)<1:
    print('please try agian with a vaild city name')
else:
    # only for first result this shows options and corresponding results
    option_list=list()
    for option in data_obtained[0]: 
        option_list.append(option)

    option_list.append('Exit')
    options=[
        {
            'type': 'checkbox',
            'name': 'weather_options',
            'message': 'Select which option to show',
            'choices': option_list
        }
    ]
    
    choice=prompt(options)
    if choice['weather_option']=='Exit':
        print('Thank you for using weather service')
    else:
        print(data_obtained[0][choice['weathe_option']])

## to do
# add all available cities from search for user to choose
# give information in more clean format 