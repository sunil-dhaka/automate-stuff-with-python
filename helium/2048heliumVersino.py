from os import read
from helium import *
from time import sleep

web=start_chrome()
go_to('play2048.co')
sleep(2)
for i in range(3):
    while not Text('try again').exists():
        ele=find_all(S('div.score-container'))
        press(UP)
        press(RIGHT)
        press(DOWN)
        press(LEFT)
        
    print('score is ',ele[0].web_element.text)
    sleep(2)
    click('try again')
    print(str(i+1), 'th play completed')
'''
to speed up a bit we can run a for loop inside while condition so that it does not check the cond after every four moves
'''