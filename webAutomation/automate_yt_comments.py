"""
author: @sunil-dhaka
simple script to comment on download videos from a channel
"""
from lib2to3.pgen2 import driver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
from helium import *
from time import sleep
import pyautogui
import numpy as np
import sys
import youtube_dl
import login

# to be able to control window dor one second when things go south
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True

if len(sys.argv)>1:
    channel_id=sys.argv[1]
else:
    print('please give an valid channel id')
    sys.exit()

def google_login_undetecteed():
    gmail=login.gmail
    password=login.password

    chrome_options=uc.ChromeOptions()

    chrome_options.add_argument("--disable-extensions")

    chrome_options.add_argument("--disable-popup-blocking")

    chrome_options.add_argument("--profile-directory=Default")

    chrome_options.add_argument("--ignore-certificate-errors")

    chrome_options.add_argument("--disable-plugins-discovery")

    chrome_options.add_argument("--incognito")

    chrome_options.add_argument("user_agent=DN")

    chrome_options.add_argument("--start-maximized")

    # chrome_options.add_argument("--headless") # TODO: running headless giving error
    driver = uc.Chrome(options=chrome_options)

    driver.delete_all_cookies()

    driver.get("https://accounts.google.com/")
    sleep(2)
    driver.find_element(by='xpath',value="//*[@id='identifierId']").send_keys(gmail)
    sleep(0.5)
    driver.find_element(by='xpath',value="//*[@id='identifierNext']/div/button").send_keys(Keys.RETURN)
    sleep(2)
    driver.find_element(by='xpath',value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    sleep(0.5)
    driver.find_element(by='xpath',value="//*[@id='passwordNext']/div/button").send_keys(Keys.RETURN)
    print(f'SUCCESS! Logged into {gmail} account.')
    sleep(2)

    return driver

driver=google_login_undetecteed()
base_url='https://www.youtube.com/watch?v='

INTERVAL=0.1
sleep(2)
print('2 secs to switch to the main window.')

channel_url=f'https://www.youtube.com/c/{channel_id}'

ydl=youtube_dl.YoutubeDL()
channel_data=ydl.extract_info(channel_url,download=False)

# by trail  and error found where id data is 
video_data=channel_data['entries'][0]['entries']

print('total videos found ... ',len(video_data))

for i,info in enumerate(video_data): # due to interent issue only 4 vids to test
    print('working on -- ',{i+1})
    link=base_url+info['id']
    driver.get(link)
    sleep(10)
    driver.execute_script("window.scrollTo(0,1000)")
    sleep(10)
    commentable=True
    try:
        driver.find_element(by='id',value='simplebox-placeholder')
    except NoSuchElementException:
        commentable=False

    if commentable:
        sleep(2)
        """
        gui automation
        needs to keep this frame in front layer
        """
        # click into the comment box
        pyautogui.click(205,316)
        sleep(1)
        comment_message='SUBSCRIBE this channel for good quality free educational videos.'
        pyautogui.typewrite(comment_message,interval=INTERVAL)
        sleep(1)
        pyautogui.typewrite(['\t','\t','\n'],interval=INTERVAL)
        sleep(1)
        print(f'Commented for video {i+1}')
    else:
        print(f'Video {i+1} has comments turned off.')
    