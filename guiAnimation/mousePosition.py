import pyautogui,sys
pyautogui.PAUSE=0.5
pyautogui.FAILSAFE=True

def mousePosition():
    print('Press Ctrl-C to quit.')
    while(True):
        try:
            x,y=pyautogui.position()
            pixelColor=pyautogui.screenshot().getpixel((x,y))
            # specifically tailered string by error and trial
            print_str=f'X:{str(x).zfill(4)}  Y:{str(y).zfill(4)} RGB: {pixelColor}'
            print(f'{print_str}',end='',flush=True) # flush is important for nice printing
            print('\b'*len(print_str),end='') # end is most important
        except KeyboardInterrupt:
            # print('Stopped')
            sys.exit()

if __name__=="__main__":
    mousePosition()