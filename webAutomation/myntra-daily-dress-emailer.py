
import requests
from bs4 import BeautifulSoup as bs
import smtplib

def getPrice(link):
    r=requests.get(link)
    print(r.status_code)
    localSoup=bs(r.text,features='html.parser')
    productPrice= localSoup.find('span',class_='pdp-price').get_text().strip()[4:] # to not include 'Rs. '
    print(productPrice)
    return productPrice

def addPrices(p1,p2,p3):
    return float(p1)+float(p2)+float(p3)

def sendMail(email,passwd,towhom):
    newserver=smtplib.SMTP('smtp.gmail.com',587) #<-- 587 is the port no that gmail server uses
    newserver.starttls() # Transport Layer Security Protocol
    newserver.login(email,passwd)
    subject=f'Price to not be naked today'
    body=f'You need to own {totalPrice} to be able to look dashing and also not naked.\n - To wear sandle pair need Rs. {sandle}\n -To wear a shirt need Rs. {shirt}\n -To wear a pant need Rs. {pant}\n PS: personaly I would wear nothing(::) than waste {totalPrice} on these shitty.\n\nSincerely,\nYour Dress Buyer Bot'
    message=f'Subject:{subject}\n\n{body}\nDo not give mintra your hard earned money. Wait and let me see if prices drop ...'
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