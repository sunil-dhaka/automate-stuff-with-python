"""
author: @sunil-dhaka
use: script to remove background from images using removebg api tool
# further features also can be added ilke this one: https://github.com/brilam/remove-bg
"""

import requests
import argparse

import login

def removebg(file_path,size='small'):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(file_path, 'rb')},
        data={'size': size,'scale':'50%'},
        headers={'X-Api-Key': login.remove_bg_api_key}, # need to create your key and add it here
        )
    
    if response.status_code==requests.codes.ok:
        with open('bg_removed.png','wb') as file:
            file.write(response.content)
    else:
        print('Error:', response.status_code, response.text)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--file',required=True,help='path to the image file')
    args=parser.parse_args()
    removebg(args.file)
