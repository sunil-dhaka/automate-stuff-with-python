from PIL import Image, ImageDraw,ImageFont
import os
'''
font setting
'''
font_folder='/home/sunild/.fonts'
monacoFont=ImageFont.truetype(os.path.join(font_folder,'monaco.ttf'),20)
smallMonaco=ImageFont.truetype(os.path.join(font_folder,'monaco.ttf'),10)
'''
create new canvas
'''
im=Image.new('RGBA',(1920,1080),'white')
drawIm=ImageDraw.Draw(im)
'''
line
'''
drawIm.line([(0,0),(100,100),(200,200),(0,200)],fill='red',width=5)
drawIm.text((100,50),'line',fill='purple',font=monacoFont)
'''
points
'''
# why points are clearly visible; but they are there
drawIm.point([(400,200),(300,500),(200,600),(100,700),(0,800)],fill='red')
drawIm.text((200,600),'point',fill='purple',font=smallMonaco)
drawIm.text((300,500),'point',fill='purple',font=smallMonaco)
drawIm.text((400,200),'point',fill='purple',font=smallMonaco)
drawIm.text((100,700),'point',fill='purple',font=smallMonaco)
drawIm.text((0,800),'point',fill='purple',font=smallMonaco)
'''
rectangle and ellipse
'''
drawIm.rectangle((500,500,800,800),width=5,outline='red')
# filled rectangle
drawIm.rectangle((650,650,750,750),width=2,fill='purple',outline='red')
drawIm.ellipse((500,500,800,800),width=5,outline='red')
# filled ellipse
drawIm.ellipse((650,650,750,750),width=2,fill='white',outline='red')
drawIm.text((800,800),'ellipse/circle/rectangle',fill='purple',font=monacoFont)
'''
polygon
'''
# a polygon
drawIm.polygon([(400,400),(850,500),(900,800),(900,300),(600,300)],fill=(29,29,29,40),outline='green')
drawIm.text((900,500),'polygon',fill='purple',font=monacoFont)

'''
all three methods move in counter-clockwise like rotate
arc
chord
pieslice
'''
# an arc in circle/ellipse box
drawIm.arc((1500,200,1700,400),0,240,fill='green',width=5)
drawIm.text((1500,250),'arc',fill='purple',font=monacoFont)

# an chords in circle/ellipse box
drawIm.chord((1300,200,1400,300),0,240,fill=(100,200,120,100),width=5)
drawIm.text((1400,200),'chord',fill='purple',font=monacoFont)

# an pieslice in circle/ellipse box
drawIm.pieslice((1100,200,1300,400),0,70,fill=(100,200,120,100),width=5)
drawIm.text((1250,350),'pieslice',fill='purple',font=monacoFont)
'''
box around text
sol: create a ractangle and write text in it
'''
print(monacoFont.getsize('pieslice'))
drawIm.text((1250,350),'pieslice',font=monacoFont,anchor='mm',fill='black')
# save image
im.save('drawImage.png')
# im.show()