import requests
from bs4 import BeautifulSoup as bs
import os
from datetime import date
import json
###### uncomment a link and work with it
link='https://web.archive.org/web/20200312001206/http://radio.garden/api/content/places'
#link='http://radio.garden/api/ara/content/places' # --the best resource
#link='http://radio.garden/api/ara/content/page/W9g0lZfQ'
#link='http://radio.garden/api/ara/content/channel/tMGsmGxF'
#link='http://radio.garden/api/ara/content/listen/tMGsmGxF/channel.mp3'
######
r=requests.get(link)
print('Status from link, ',r.status_code)
soup=bs(r.text,features='html.parser')
print(type(soup))
# convert bs4.BeautifulSoup into dictionary
data_dict=json.loads(str(soup)) # <------- imp step othervise can not work with tree structure
print('total no of keys in first level dict: ',len(data_dict))
print('api verion: ',data_dict['apiVersion'])
print('radio data version: ',data_dict['version'])
radio_data_dict=data_dict['data']['places']['list'] # this needs to be changes with other links
print('total no of radio available in radio-garden version:',data_dict['version'],'are ----> ',len(radio_data_dict),' <-----')
## what to do with this nice and cheap data
# radio-garden itself is a nice product 
# can make a connector from terminal 
# get a list of all radio station website and give it to rhythmbox