'''
author: @sunil-dhaka
script to extract audio from given video file(s)
'''
from moviepy.editor import VideoFileClip
import os

def extractAudio(inputClips,ext='mp3'):
    '''
    using moviepy
    
    input:
        inputClips: input video files
        ext: output audio file extension
    '''
    print('Using moviepy method.')
    # read video clips using 'VideoFileClip
    clips=[VideoFileClip(clip) for clip in inputClips]
    clip_names=[os.path.splitext(file)[0]+'.'+ext for file in inputClips]
    # TRICK: write only audio of video files into output; file.audio.write_audio()
    for i,clip in enumerate(clips):
        print('Extracting ... ', clip_names[i])
        clip.audio.write_audiofile(clip_names[i])
        print('Extracted and saved @', clip_names[i])

def parser():
    myParser=argparse.ArgumentParser(description='script to extrcat audio form video file(s)',prog='extractAudio',epilog='Useful script. author: @sunil-dhaka')
    myParser.add_argument(
        '-i',
        '--input',
        nargs='+',
        required=True,
        help='input video file(s) name/path'
    )
    myParser.add_argument(
        '-e',
        '--extension',
        default='mp3',
        help='output audio file extension'
    )
    return myParser.parse_args()

if __name__=="__main__":
    import argparse,time
    myParser=parser()
    tic=time.time()
    extractAudio(myParser.input,myParser.extension)
    toc=time.time()
    print(f'time taken to concat video clips -- {round(toc-tic)} secs')