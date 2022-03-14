from PIL import Image
import os,sys

def tileImage(source_image,canvas_image='blank'):
    '''
    Input:
        source_image: source image that needs to be tiled on top of canvas\\
        canvas_image: default is white blank canvas of size(1920,1080), can set a particular image
    '''
    sourceImage=Image.open(source_image)
    w,h=sourceImage.size
    if canvas_image=='blank':
        W=1920
        H=1080
        canvasImage2=Image.new('RGBA',(W,H),'white')
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

    for width in range(0,W,w):
        for height in range(0,H,h):
            # print(width,height)
            canvasImage2.paste(sourceImage,(width,height))
    
    canvasImage2.save(base_path+file_name+'_tiled.png')
    print('Completed tiling.')
    
if __name__=="__main__":
    if len(sys.argv)<2:
        print('Usage: tile source-image on blank calvas or on image')
        print('Input: <source_image> <canvas_image>[image that is used as canvas for tiling;optional;blank white canvas is default]')
        sys.exit()
    sourceImage=sys.argv[1]
    try:
        canvasImage=sys.argv[2]
    except IndexError:
        canvasImage='blank'
    tileImage(sourceImage,canvasImage)