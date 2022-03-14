from PIL import Image
import os,sys

def getImageInfo(image_source):
    image=Image.open(image_source)
    print(''.center(40,'='))
    print('filename --',os.path.abspath(image.filename))
    print('size --',round(os.path.getsize(image_source)/1024,1), 'KB')
    print('width --',image.width)
    print('height --',image.height)
    print('format --',image.format)
    print(''.center(40,'='))

if __name__=="__main__":
    if len(sys.argv)<2:
        print('Usage: gets info about input-image-file and prints')
        sys.exit()
    fileName=sys.argv[1]
    getImageInfo(fileName)
