import os
from time import sleep
from selenium import webdriver

# firefox options are not working for me
'''
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

options = FirefoxOptions()
options.set_preference("browser.download.folderList", 1)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf;text/plain;application/text;text/xml;application/xml;application/vnd.adobe.dc+json")
'''
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
        driver = webdriver.Chrome()

        driver.get('https://www.adobe.com/in/acrobat/online/ppt-to-pdf.html')

        try:
            print('Sleeping for 2 secs ...')
            sleep(3)

            print(f'Dragging >>> {file}')
            driver.find_element_by_xpath('//*[@id="fileInput"]').send_keys(os.getcwd()+'/'+file)

            sleep(60)
            
            print('Downloading ...')
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/section[2]/div/div[1]/div[2]/button[1]').click()
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
            driver.quit()
            return

        except Exception as e:
            print(e)
            driver.quit()
            return

for file in files_list:
    if '.pptx' in file:
        pptTopdfAdobe(file)
    else:
        print('File is not the right one for converter.')