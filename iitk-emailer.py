from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.firefox.options import Log

link='https://webmail.iitk.ac.in/'

webmail=webdriver.Chrome()
webmail.get(link)

new_webmail=webmail.find_element_by_xpath('/html/body/div/div[3]/div[4]')
new_webmail.click()
user=input('username: ')
pwd=input('password: ')
username=webmail.find_element_by_id('rcmloginuser')
passwd=webmail.find_element_by_id('rcmloginpwd')
username.send_keys(user)
passwd.send_keys(pwd)
passwd.submit()

print('waiting to load page ...')
time.sleep(5)
compose=webmail.find_element_by_xpath('//*[@id="rcmbtn109"]')
compose.click()
print('waiting for composer to load ...')
time.sleep(5)

dest=input('to whom: ')
sub=input('subject: ')
message=input('what is your message: ')
try:
    destination=webmail.find_element_by_xpath('//*[@id="compose_to"]/div/div/ul/li/input')
    subject=webmail.find_element_by_xpath('//*[@id="compose-subject"]')
    #------------------------------------------------------
    # message is creating some issues
    # want to send a mail without message :: nah
    # need solution --> send message to right element
    '''#body=webmail.find_element_by_xpath('//*[@id="tinymce"]')
    plainText=webmail.find_element_by_xpath('//*[@id="mceu_26-button"]/i')
    plainText.click()
    time.sleep(2)
    body=webmail.find_element_by_xpath('//*[@id="composebody"]')'''
    #--------------------------------------------------------
    draft=webmail.find_element_by_xpath('//*[@id="rcmbtn110"]')
    send=webmail.find_element_by_xpath('//*[@id="rcmbtn115"]')
    destination.send_keys(dest)
    subject.send_keys(sub)
    #body.send_keys(message)
    print('waiting to save ... ')
    time.sleep(5)
    draft.click()
    print('waiting to send ...')
    time.sleep(5)
    send.click()
    print('waiting to logout ...')
    time.sleep(20)
    logout=webmail.find_element_by_xpath('//*[@id="rcmbtn109"]')
    logout.click()
    webmail.quit()
    print('window closed')
except Exception as e:
    print('Your programme has [%s] problem.'%e)
    webmail.quit()
    print('window closed')
#-------------------------------------------------------------    
############ NOTES
#tip: easily copy xpath of an element in chrome by right clicking the element
#to login into old_webmail have to type captcha and that is a tough job:
# possible soutions -- use api of some service to give you text
# link1: https://stackoverflow.com/questions/18935696/how-to-read-the-text-from-image-captcha-by-using-selenium-webdriver-with-java
# link2: https://medium.com/@vineet_c/using-tesseract-to-solve-captcha-while-logging-in-to-a-website-with-selenium-899a810cf14
###########