import requests
from PyInquirer import prompt

def gettingBored(type):
    url=f'http://www.boredapi.com/api/activity?type={type}'
    r=requests.get(url).json()
    print('Do this'.center(50,'🎸'))
    print('To do'.ljust(20,'-')+(r['activity']).rjust(30))
    print('Participants'.ljust(40,'-')+str(r['participants']).rjust(10))
    print('Price'.ljust(40,'-')+str(r['price']).rjust(10))


activityList=["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
whichType=[
    {

        'type':'list',
        'name':'activity',
        'message':'which activity you want to do >>>',
        'choices':activityList
    }
]

answer=prompt(whichType)
type=answer['activity']

gettingBored(type)