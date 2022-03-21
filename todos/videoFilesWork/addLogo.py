"""
author: @sunil-dhaka
usage: simple script to add logo on a video file(s)
"""
import argparse
import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

POSITIONS={
    'l':'left',
    'r':'right',
    'b':'bottom',
    't':'top'
}
SIZE=50
def addLogo(video_file,logo_file,size=SIZE,position=['r','t']):
    """
    simple function to add logo on a video with specified size and position
    """
    # get video-file name and base path
    split_path=os.path.abspath(video_file).split('/')
    base_path='/'.join(split_path[:-1])
    file_name=split_path[-1]

    # read video and logo file and make composite video clip and write in new video file
    video_clip=VideoFileClip(video_file)
    logo_image=ImageClip(logo_file).set_duration(video_clip.duration).resize(height=size).set_pos((POSITIONS[position[0]],POSITIONS[position[1]]))
    logo_added_clip=CompositeVideoClip([video_clip,logo_image])
    logo_added_clip.write_videofile(f'{base_path}/logo_{file_name}')

def parser():
    """
    parser function to parse arguments taken from user 
    """
    myParser=argparse.ArgumentParser(
        prog='addLogo',
        epilog='author: @sunil-dhaka',
        description='simple script to add logo on a video file(s)'
    )
    myParser.add_argument(
        '-v',
        '--video',
        help='video file(s) path(s)',
        nargs='+',
        required=True
    )
    myParser.add_argument(
        '-l',
        '--logo',
        help='logo image file path',
        required=True
    )
    myParser.add_argument(
        '-s',
        '--size',
        help='logo size(height) in pixel'
    )
    myParser.add_argument(
        '-p',
        '--position',
        help='logo position on video file. options are: (l,t) | (l,b) | (r,t) | (r,b)',
        nargs='+'
    )
    return myParser.parse_args()

if __name__=="__main__":
    myParser=parser()
    # to check whether size input is given or not
    if myParser.size is None:
        size=SIZE # set deafult to 50(SIZE) pixels
    else:
        size=int(myParser.size)
    # to check position argument
    if myParser.position is None:
        position=['r','t'] # set default to top-right
    else:
        position=[myParser.position[0],myParser.position[1]]

    for video_file in myParser.video:
        addLogo(video_file,myParser.logo,size,position)
        print(f'completed : {video_file}')