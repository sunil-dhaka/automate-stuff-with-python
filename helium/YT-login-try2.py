from helium import *
from time import sleep
import logindetails

class Youtube:

    def __init__(self,username,password):

        start_chrome()
        go_to('https://youtube.com')
        sleep(5)
        click(Button('Sign in'))
        write(username,into='Email')
        sleep(3)
        click('Next')
        sleep(3)
        if Button('Try again').exists():
            print('It is some BS.')
            kill_browser()
        else:
            write(password,into='Password')
            click('Next')
            if Button('Not now').exists():
                click(Button('Not now'))
            sleep(2)
            print('You got it, lets play some videos.')

username=logindetails.user
password=logindetails.passwd

Youtube(username,password)

#========
# google is not going to let auto sign using selenium
# I tried after turning off 2FA and even less secure app but won't buzz
# google is shit
# even this does not have a solution:
# -->https://gist.github.com/ikegami-yukino/51b247080976cb41fe93
# I am not going to work on it now
#========