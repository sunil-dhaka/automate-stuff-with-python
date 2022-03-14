from PIL import Image, ImageDraw
import os,sys

'''
Resizes all images in current working directory to fit
in a 300x300 square
'''
SQUARE_FIT_SIZE=300
LOGO_FIT_SIZE=20
BLANK_CANVAS_W=1920
BLANK_CANVAS_H=1080

def addLogo(logo_image,canvas_image='blank'):
    '''
    Input:
        logo_image: logo image that needs to be pasted/added on top of canvas\\
        canvas_image: default is white blank canvas of size(1920,1080), can set a particular image
    '''
    logoImage=Image.open(logo_image)
    # resize logo image
    logoImage=logoImage.resize((LOGO_FIT_SIZE,LOGO_FIT_SIZE))
    print('Resized logo image to -- ',(LOGO_FIT_SIZE,LOGO_FIT_SIZE))

    if canvas_image=='blank':
        canvasImage2=Image.new('RGBA',(BLANK_CANVAS_W,BLANK_CANVAS_H),'white')
        base_path=os.getcwd()+'/'
        file_name='whiteCanvas'
    else:
        # work on image filename
        path_=os.path.abspath(canvas_image).split('/')
        file_name=path_[-1].split('.')[0] # without ext
        base_path='/'.join(path_[:-1])+'/'
        canvasImage=Image.open(canvas_image)
        W,H=canvasImage.size
        # don't want to make original image messy
        canvasImage2=canvasImage.copy()

    # resize images
    # keep in mind that resize takes only int arguments >> int()
    canvasW,canvasH=canvasImage2.size
    if canvasH>canvasW and canvasH>SQUARE_FIT_SIZE:
        resizedH=SQUARE_FIT_SIZE
        resize_factor=resizedH/canvasH
        resizedW=int(canvasW*resize_factor)
        resizedH=int(resizedH)
    if canvasH<canvasW and canvasW>SQUARE_FIT_SIZE:
        resizedW=SQUARE_FIT_SIZE
        resize_factor=resizedW/canvasW
        resizedH=int(canvasH*resize_factor)
        resizedW=int(resizedW)

    canvasImage2=canvasImage2.resize((resizedW,resizedH))
    print('Resized image size -- ',(resizedW,resizedH))
    # paste logo on top left
    '''
    Remember that the paste() method will not paste
    the transparency pixels if you do not pass the logoIm for the third argument
    as well.
    '''
    canvasImage2.paste(logoImage,(0,0),logoImage)

    canvasImage2.save(base_path+file_name+'_logo.png')
    print('added logo on -- ',file_name)

if __name__=="__main__":
    if len(sys.argv)<2:
        print('Usage: add logo on an image')
        print('Input: <logo_image> <canvas_image>')
        sys.exit()
    logoImage=sys.argv[1]
    try:
        canvasImage=sys.argv[2]
    except IndexError:
        canvasImage='blank'
    addLogo(logoImage,canvasImage)