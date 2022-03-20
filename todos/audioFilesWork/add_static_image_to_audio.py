'''
author: @sunil-dhaka
use: how to add a static image to an audio file to form a video file with Python using the MoviePy library
'''

'''
imports
'''
from moviepy.editor import AudioFileClip, ImageClip
import argparse
'''
main function
'''
def addStaticImage(image_file,audio_file,video_file='output.mp4',fps=1):
    '''
    to add a static image to an audio file to form a video file\\
    Input:
        audio_file: audio file name/path
        image_file: image file name/path
        video_file: output video file name/path; default='output.mp4'
        fps: fps of video file
    '''
    # read audio and image
    audioFile=AudioFileClip(audio_file)
    imageFile=ImageClip(image_file)
    # set video parameters
    videoFile=imageFile.set_audio(audioFile)
    videoFile.duration=audioFile.duration
    videoFile.fps=fps
    # write video file
    videoFile.write_videofile(video_file)

'''
parser function
'''
def parser():
    myParser=argparse.ArgumentParser(
        prog='addStaticImage',
        description='how to add a static image to an audio file to form a video file with Python using the MoviePy library'
    )
    myParser.add_argument(
        'image',
        # required=True,
        help='image file path'
    )
    myParser.add_argument(
        'audio',
        # required=True,
        help='audio file path'
    )
    myParser.add_argument(
        'video',
        # required=True,
        help='video file path'
    )
    return myParser.parse_args()

if __name__ == '__main__':
    myParser=parser()
    addStaticImage(myParser.image,myParser.audio,myParser.video)