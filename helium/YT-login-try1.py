from helium import *
from time import sleep
import logindetails

class Youtube:

    def __init__(self,displayname,username,password):

        start_chrome()
        go_to('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
        sleep(5)
        write(displayname,into='Display name')
        write(username,into='Email')
        write(password,into='Password')
        sleep(2)
        click("I'm not a robot") # image click captcha appears does not seem to work
        click('Sign up')         # but when clicked manually it just does not show
        sleep(5)                 # Google fixed this, not an options anymore
        go_to('https://youtube.com')
        sleep(2)

displayname=input('what do you want to be called -- ')
username=logindetails.user
password=logindetails.passwd

Youtube(displayname,username,password)
kill_browser()