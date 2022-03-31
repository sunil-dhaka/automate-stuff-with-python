"""
author: @sunil dhaka
this is a simple script that take a video file and an audio file as input; from them it creates a musical video without audio on top of video file
"""
from email.mime import base
import os
import argparse
from moviepy.editor import VideoFileClip, AudioFileClip

def makeMusical(video_file,audio_file=None):
    """
    function to remove audio from a video clip and given audio file, 
    in case no audio file it just removes audio from video clip and returns video
    """
    splited_path=os.path.abspath(video_file).split('/')
    base_path='/'.join(splited_path[:-1])
    video_file_name=splited_path[-1]
    video_clip=VideoFileClip(video_file)
    video_clip_wo_audio=video_clip.without_audio()
    if audio_file is not None:
        audio_clip=AudioFileClip(audio_file)
        new_musical_video_clip=video_clip_wo_audio.set_audio(audio_clip)
        new_musical_video_clip.write_videofile(os.path.join(base_path,'musical_'+video_file_name))
    else:
        video_clip_wo_audio.write_videofile(os.path.join(base_path,'musical_'+video_file_name))

def parser():
    myParser=argparse.ArgumentParser(
        description='script to take a video file and an audio file as input; from them it creates a musical video without audio on top of video file; and if audio file is not given then it just creates a simple video file with no audio',
        prog='makeMusical',
        epilog='author: @sunil dhaka'
    )
    myParser.add_argument(
        '-v',
        '--video',
        help='video file path',
        required=True
    )
    myParser.add_argument(
        '-a',
        '--audio',
        help='audio file path',
    )
    return myParser.parse_args()

if __name__=="__main__":
    myParser=parser()
    if myParser.audio is not None:
        makeMusical(myParser.video, myParser.audio)
    else:
        makeMusical(myParser.video)