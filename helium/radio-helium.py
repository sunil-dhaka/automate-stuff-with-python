from helium import *

# works on https://www.radioindia.in/purani-jeans with click>btn>Play :: but how to pause it??
url='radio.garden'
start_chrome()
go_to(url)
Config.implicit_wait_secs=5
try:
    click(Button('Play'))
except Exception as e:
    print(e)
    kill_browser()
