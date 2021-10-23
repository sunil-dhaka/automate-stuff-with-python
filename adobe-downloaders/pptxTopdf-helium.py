import os
from helium import *
from time import time,sleep

# none of them worked #

# from selenium import webdriver
# from selenium.webdriver import Firefox
# from selenium.webdriver import FirefoxOptions
# options = FirefoxOptions()
# # options.add_argument("--width=2560")
# # options.add_argument("--height=1440")
# options.set_preference("browser.download.folderList", 1)
# # 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use the directory 
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf;text/plain;application/text;text/xml;application/xml;application/vnd.adobe.dc+json")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf;application/vnd.adobe.dc+json;text/plain;text/xml")
# # start_firefox(options=options)
# # fp=webdriver.FirefoxProfile()
# # fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf;text/plain;application/text;text/xml;application/xml")

######## os work ########
# takes a list of 
print('path to the folder where files are? Relative path files are also allowed. leave blank for cwd as path >>> ')
path=input()

if path=='':
    path=os.getcwd()
    print('Given dir is >>',os.getcwd())
else:
    if os.path.isdir(path):
        os.chdir(path)
        print('Given dir is >>',path)
    else:
        print('give a valid directory')
        exit()

files_list=os.listdir()

######## main converter functoin ########
def pptTopdfAdobe(file):
    global options
    converting_from='.pptx'
    converting_to='.pdf'
    converted_file_name=file.replace(converting_from,converting_to)
    download_list=os.listdir('/home/sunild/Downloads') #<-- your browsers default downloading folder path

    # if already file exists then does not download
    if converted_file_name in download_list:
        print(f'already {converted_file_name} exists')
    else:
        start_firefox(headless=False) #,options=options 
        # driver = webdriver.Firefox(firefox_profile = fp)
        '''
        headless does not work at least not in chrome
        it does work with firefox but first check wether pdf downloading is auto-allowed or not
        otherwise have to work around that little firefox pop we get when downloading an unknown type of file
        OR
        I am not able to do it right now >> whenever I change the setting it only applies for that session only
        But our base for converting multiple times is changing the session for each file; so that is not good
        Might try: https://stackoverflow.com/questions/36309314/set-firefox-profile-to-download-files-automatically-using-selenium-and-java

        TODO:
        try out: firefox webdriver options setting
        '''
        # driver.get('https://www.adobe.com/in/acrobat/online/ppt-to-pdf.html')

        go_to('https://www.adobe.com/in/acrobat/online/ppt-to-pdf.html')
        try:
            print('Sleeping for 2 secs ...')
            sleep(3)

            print(f'Dragging >>> {file}')
            drag_file(path+'/'+file,to='Select a file')
            print('Sleeping for 30+ secs ...')
            sleep(30)
            waitTime=0
            while(not Button('Download').exists() and waitTime<=30):
                sleep(5)
                waitTime+=5

            #==== this wait does not seems to works >> giving a fixed 30 sec window
            
            '''
            tic=time()
            print('Uploading ...')
            wait_until(lambda: not Text("Uploading...").exists(),timeout_secs=30)
            print(f'Completed uploading of {file}')
            toc=time()
            print(f'Time taken to upload {file} is {toc-tic} seconds')    
            '''

            # check if file is downloaded or not 

            print('Downloading ...')
            sleep(2)
            click('Download')

            waitTime=0
            while((converted_file_name not in download_list) and (waitTime<=30)):

                # update after every 5 secs
                sleep(5)
                waitTime+=5
                download_list=os.listdir('/home/sunild/Downloads')

            if converted_file_name in download_list:
                print(f'Downloaded >>> {converted_file_name}')
            else:
                print('Opps! Slow internet.')
            kill_browser()
            return

        except Exception as e:
            print(e)
            kill_browser()
            return

for file in files_list:
    if '.pptx' in file:
        pptTopdfAdobe(file)
    else:
        print('File is not the right one for converter.')