'''
author: @sunil-dhaka
use: script to get exif info of images; only applies to JPEG format images
todo: add wildcard expension functionality
'''
from PIL import Image
from PIL.ExifTags import TAGS
import argparse,os


def getExifInfo(files):
    for file in files:
        if os.path.splitext(file)[1].lower()=='.jpg':
            im=Image.open('/home/sunild/Pictures/Photos/Pics-of-Mine/winter-dressing/IMG_20211201_125719.jpg')
            info=im.getexif()
            print(f'working on -- {file}')
            print(''.center(50,'-'))
            for tag in info:
                id=TAGS.get(tag,tag)
                readable_data=info.get(id)
                if isinstance(readable_data,bytes):
                    readable_data=readable_data.decode()
                # only print actual info that is not none
                if readable_data is not None:
                    print(f'{id:25}:{readable_data}')
            im.close()
            print(''.center(50,'='))
        else:
            print(f'{file} is not of JPEG format.')
if __name__=='__main__':
    parser=argparse.ArgumentParser(
        prog='getExifInfo',
        description='script to get exif info of images; only applies to JPEG format images'
    )
    parser.add_argument(
        '-i',
        '--input',
        nargs='+', # one or more
        required=True,
        help='input image file(s)'
    )
    myParser=parser.parse_args()
    getExifInfo(myParser.input)