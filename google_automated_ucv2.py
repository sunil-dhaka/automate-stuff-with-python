import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
from helium import *
from time import sleep
import login

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

driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(gmail)
sleep(2)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").send_keys(Keys.RETURN)

sleep(2)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
sleep(2)
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").send_keys(Keys.RETURN)
sleep(3)
driver.get('https://www.youtube.com/c/sbnclasses') # channel link as user input and number videos to be commented # or could give particular video link
sleep(2)
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]').send_keys(Keys.RETURN)
sleep(10)
html=driver.page_source
soup=bs(html,'html.parser')

video_links=['https://www.youtube.com'+video.find(id='thumbnail').get('href') for video in soup.find('div',id='content').find_all('ytd-grid-video-renderer')]

for link in video_links[1:5]: # due to interent issue only 4 vids to test

    driver.get(link)
    sleep(5)
    driver.execute_script("window.scrollTo(0,1000)")
    sleep(5)
    try:
        comment_box=driver.find_element_by_id('simplebox-placeholder')
        sleep(3)
        comment_box.send_keys('This channel does have 🌟good quality🌟 video conetnt. Keep it up SBNCLASSES. 👍')
    except NoSuchElementException:
        print('comments are off for this video.')
        sleep(2)
        continue
    sleep(2)
    comment_submit=driver.find_element_by_css_selector("tp-yt-paper-button[aria-label='Comment']")
    sleep(1)
    comment_submit.send_keys(Keys.RETURN)
    sleep(2)
