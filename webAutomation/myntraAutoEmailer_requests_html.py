'''
actually previous myntra versino does not work(since myntra uses JS) so I have created this new one that
- uses helium to get page sources
- and then using BS we parse that html page to get prices
'''

from helium import *
from bs4 import BeautifulSoup as bs
import smtplib
from time import sleep
def getPrice(link):
    myntraShop=start_chrome()
    go_to(link)
    sleep(5)
    html=myntraShop.page_source
    soup=bs(html,'html.parser')
    price=soup.find_all('span',class_='pdp-mrp-verbiage-amt')[-1].string.strip()[4:]
    print(price)
    kill_browser()
    return int(price)

def addPrices(p1,p2,p3):
    return float(p1)+float(p2)+float(p3)
def sendMail(email,passwd,towhom):
    global totalPrice
    newserver=smtplib.SMTP('smtp.gmail.com',587) #<-- 587 is the port no that gmail server uses
    newserver.starttls() # Transport Layer Security Protocol
    newserver.login(email,passwd)
    subject=f'Price to not be naked today'
    body=f'You need to own {totalPrice} to be able to look dashing and also not naked.\n - To wear sandle pair need Rs. {sandle}\n - To wear a shirt need Rs. {shirt}\n - To wear a pant need Rs. {pant}\n\nSincerely,\nYour Dress Buyer Bot'
    message=f'Subject:{subject}\n\n{body}'
    newserver.sendmail(email,towhom,message)
    print('Email has been sent to %s'%(towhom))
    newserver.quit()

sandle = getPrice('https://www.myntra.com/sports-sandals/wildcraft/wildcraft-men-black-ride-sports-sandals/15039012/buy')
shirt = getPrice('https://www.myntra.com/shirts/nautica/nautica-men-white--blue-slim-fit-printed-casual-shirt/13768798/buy')
pant = getPrice('https://www.myntra.com/track-pants/arrow-sport/arrow-sport-men-black-solid-straight-fit-track-pants/15337108/buy')

totalPrice=addPrices(sandle,shirt,pant)
print('total price is ----> Rs. ',totalPrice)

email=input('Which email to use --')
passwd=input('What is the password , if you even remember --')
towhom=input('Where you want to go in this vast network --')
sendMail(email,passwd,towhom)