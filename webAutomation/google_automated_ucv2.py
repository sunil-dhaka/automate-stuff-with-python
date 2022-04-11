import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from bs4 import BeautifulSoup as bs
from helium import *
from time import sleep
import pyautogui
import numpy as np

# to be able to control window dor one second when things go south
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True


import login

def google_login_undetecteed():
    pass

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

"""
this is done to get the video ids and one can get them using youtube-dl as well 
"""
# driver.get('https://www.youtube.com/c/CHAHATKITCHEN/videos') # channel link as user input and number videos to be commented # or could give particular video link
# sleep(5)
# driver.find_element(by='xpath',value='/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]').send_keys(Keys.RETURN)
# sleep(10)
# html=driver.page_source
# soup=bs(html,'html.parser')
# comments_=['automated. nice video']
video_links=['https://www.youtube.com'+video.find(id='thumbnail').get('href') for video in soup.find('div',id='content').find_all('ytd-grid-video-renderer')]
INTERVAL=0.1
sleep(5)
print('5 secs to switch to the main window.')

for i,link in enumerate(video_links[4:]): # due to interent issue only 4 vids to test
    driver.get(link)
    sleep(5)
    driver.execute_script("window.scrollTo(0,1000)")
    sleep(5)
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
        comment_message='SUBSCRIBE this channel for all good and simple recipes. for educational content: https://www.youtube.com/c/SBNCLASSES; Note: automated comment by bot.'
        pyautogui.typewrite(comment_message,interval=INTERVAL)
        sleep(1)
        pyautogui.typewrite(['\t','\t','\n'],interval=INTERVAL)
        sleep(1)
        print(f'Commented for video {i+1}')
    else:
        print(f'Video {i+1} has comments turned off.')
    
    """
    currently not working; gives 'element not interactable error'
    """
    # driver.find_element(by='id',value='simplebox-placeholder').send_keys('This channel does have 🌟good quality🌟 video conetnt. Keep it up SBNCLASSES. 👍')
    # sleep(2)
    # comment_submit=driver.find_element_by_css_selector("tp-yt-paper-button[aria-label='Comment']")
    # sleep(1)
    # comment_submit.send_keys(Keys.RETURN)
    # sleep(2)
