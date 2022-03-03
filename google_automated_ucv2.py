from lib2to3.pgen2 import driver
import undetected_chromedriver.v2 as uc
import random,time,os,sys
from selenium.webdriver.common.keys import Keys
from helium import *
import login
"""
driver.find_element_by_id('simplebox-placeholder')
tmp.send_keys('This is an automated comment from a bot that I created. I am using this channel for testing purposes with owners permission.')
driver.find_element_by_css_selector("tp-yt-paper-button[aria-label='Comment']")
"""
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

driver = uc.Chrome(options=chrome_options)
# driver=start_chrome(options=chrome_options)
# /html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input
# //*[@id="password"]/div[1]/div/div[1]/input
# //*[@id="passwordNext"]/div/button
driver.delete_all_cookies()

# driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(gmail)
# driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").send_keys(Keys.RETURN)
time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").send_keys(Keys.RETURN)

# write('monuarun',into='Password')
# time.sleep(2)
# click('Next') 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(password)
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").send_keys(Keys.RETURN)
# //*[@id="identifierNext"]/div/button
# time.sleep(2)

# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").send_keys(Keys.RETURN)
time.sleep(3)
driver.get('https://www.youtube.com/c/sbnclasses')
time.sleep(2)
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]').send_keys(Keys.RETURN)
time.sleep(10)
button1=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]')

button1.click()
time.sleep(5)
driver.execute_script("window.scrollTo(0,1000)")
time.sleep(10)

# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[2]
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]