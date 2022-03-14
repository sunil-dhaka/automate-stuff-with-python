'''
Author: @sunil-dhaka
uncomment sections to see how they interact
I have used xournal++ application for testing these
If you are using another application then make sure you have right options set up for pyautogui
'''
import pyautogui,time

'''
gives time to swtich to paint application and set mouse
'''
time.sleep(5)

'''
this click() ensures we start doing things where mosue is right now
'''
pyautogui.click()

# pyautogui.typewrite('4')

'''
draw maze
Pen/Brush tool should be selected
'''
# dist=200

# while(dist>0):
#     pyautogui.dragRel(dist,0,duration=0.5)
#     dist-=10
#     pyautogui.dragRel(0,dist,duration=0.5)
#     pyautogui.dragRel(-dist,0,duration=0.5)
#     dist-=10
#     pyautogui.dragRel(0,-dist,duration=0.5)

'''
draw diamonds
Pen/Brush tool should be selected
why drag zig-zags in this one?
'''
# side=200

# while(side>0):
#     pyautogui.dragRel(int(side/2),int(side/2),duration=0.5)
#     side-=10
#     pyautogui.dragRel(-int(side/2),int(side/2),duration=0.5)
#     pyautogui.dragRel(-int(side/2),-int(side/2),duration=0.5)
#     side-=10
#     pyautogui.dragRel(int(side/2),-int(side/2),duration=0.5)

'''
type text
Text tool should be selected
'''
# messages=['Hello','This is an automated typed text.','To do it I have used pyautogui python module.','Thank You.']
# # non-zero interval is used to make it look like 
# for text in messages:
#     pyautogui.typewrite(text,interval=0.1)
#     pyautogui.typewrite('\n',interval=0.2)

# # to escape text box and return to application mouse
# pyautogui.mouseUp()

