#----------------------Project(webbrowser): open accuweather page based on query input-----------------#
import webbrowser, sys, pyperclip, PyInquirer
from PyInquirer import prompt

if len(sys.argv)>1:
    where_to=' '.join(sys.argv[1:])
    print('This is where you have asked to go to: ',where_to)
else:
    query=input('give query or press enter to query your clipboard:')
    if len(query)==0:
        where_to=pyperclip.paste()
        print('This is the location stored into your clipboard: ',where_to)
    else:
        where_to=query

print('I will open accuweather search results for location --> ',where_to,'. Thank you.')
webbrowser.open('https://www.accuweather.com/en/search-locations?query='+where_to)
#---------not that great--------#

## to do
# create cmdline weather result writer using accu API [at current location]
# gives options of some famous location and shows their weather
# only 50 calls for free on accu API 