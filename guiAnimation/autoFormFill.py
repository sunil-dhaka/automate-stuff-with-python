'''
author: @sunil-dhaka
Process to automate any form:
    - find out pixel co-ordinates for various parts of a form that needs to findout to start it
        - use mousePosition script to get it done easily
    - for other fields we can use keys like tab, left,down,right,up,enter
    - not just click on co-ordinates and fill info from csv/excel sheet
    - might need to scroll for a lengthy form
        - to see how to much to scroll use scroll()
            - it is simple trial and error 
    - CAN NOT CHANGE THE WINDOW WHILE THIS PROGRAMME RUNS
'''

import pyautogui, time

pyautogui.PAUSE=1


time.sleep(5)

'''
note down various co-ordinates
'''
INTERVAL=0.5
NAME_FIELD=(663,444)
'''
sample form data
'''
formData=[
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}
]


for i,data in enumerate(formData):
    print(f'Entering info for -- {data["name"]}')
    time.sleep(2)
    '''
    simple text fields
    '''
    pyautogui.click(NAME_FIELD[0],NAME_FIELD[1])
    time.sleep(1)
    pyautogui.typewrite(data['name']+'\t',interval=INTERVAL) # write name data # change into fear using 'tab'
    pyautogui.typewrite(data['fear']+'\t',interval=INTERVAL)

    '''
    butttons fields
    '''
    # selcet button
    if data['source']=='wand':
        pyautogui.typewrite(['down','\n','\t'],interval=INTERVAL)
    elif data['source']=='amulet':
        pyautogui.typewrite(['down','down','\n','\t'],interval=INTERVAL)
    elif data['source']=='crystal ball':
        pyautogui.typewrite(['down','down','down','\n','\t'],interval=INTERVAL)
    elif data['source']=='money':
        pyautogui.typewrite(['down','down','down','down','\n','\t'],interval=INTERVAL)

    # radio button
    if data['robocop']==1:
        pyautogui.typewrite([' ','\t','t'],interval=INTERVAL)
    else:
        rightList=list(['right']*(data['robocop']-1))
        rightList.append('\t')
        rightList.append('\t')
        pyautogui.typewrite(rightList,interval=INTERVAL)
    # type comments
    pyautogui.typewrite(data['comments']+'\t',interval=INTERVAL)
    # enter submit button
    time.sleep(1)
    pyautogui.typewrite('\n',interval=INTERVAL)
    
    print('submitted form')
    time.sleep(3)
    pyautogui.typewrite(['\t','\n'],interval=INTERVAL)
    time.sleep(3)