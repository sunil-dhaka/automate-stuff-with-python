#!/usr/bin/env python
import webbrowser
import PyInquirer
import time
from PyInquirer import prompt

engine='google'
## opens a new tab at particuar location
#-----specify which search engine you want to go to-----#
## give some options to choose from using prompt
which_engine=[
    {
        'type':'list',
        'name':'type',
        'message':'please choose a search engine:',
        'choices':['google','bing','duckduckgo'],
        'default':0
    }
]
answer=prompt(which_engine)
#print(answer)

engine=answer['type']

print('Please give your query text for', engine, 'search engine: ')
query=input()
print('Hurray! You are going to visit search result page for your query from terminal. Have fun doing your thing.')

time.sleep(1)

if engine!='duckduckgo':
    webbrowser.open('https://www.'+engine+'.com/search?&q='+query)
else:
    webbrowser.open('https://www.'+engine+'.com/'+query)

# documentation page: https://docs.python.org/3/library/webbrowser.html#browser-controller-objects #
#-------to make other kind of changes according to your need apply other functions to webbrowser------#