'''
author: @sunil-dhaka
todo: use tqdm to show fancy progress bar for file reading and concatening
'''
from moviepy.editor import concatenate_videoclips,VideoFileClip
import os

def moviepyConcatVideos(inputClips,outClipPath,method='compose'):
    '''
    using moviepy
    
    input:
        inputClips: input video files
        outClipPath: output concated file path
    '''
    print('Using moviepy method.')
    # read video clips using 'VideoFileClip
    clips=[VideoFileClip(clip) for clip in inputClips]
    if method=='reduce':
        # get min H and W from all video clips
        W=min([clip.w for clip in clips])
        H=min([clip.h for clip in clips])
        # resize all video clips to min H,W 
        clips=[clip.resize(newsize=(W,H)) for clip in clips]
        # concate video clips
        outFile=concatenate_videoclips(clips)
    else:
        outFile=concatenate_videoclips(clips,method="compose")
    # write concatened out file to outFilePath
    outFile.write_videofile(outClipPath)
    print('Concated and saved @', outClipPath)

def parser():
    myParser=argparse.ArgumentParser(description='script to concat multiple video files into single file',prog='concatVideos',epilog='Useful script. author: @sunil-dhaka')
    myParser.add_argument(
        '-o',
        '--output',
        required=True,
        help='name of the output concat file name/path; include ext of file'
    )
    myParser.add_argument(
        '-i',
        '--input',
        nargs='+',
        required=True,
        help='input video file names/paths'
    )
    myParser.add_argument(
        '-m',
        '--method',
        help='which method to use? compose(moviepy method) | reduce(to reduce all input clips to the lowest quality video and then concat)',
        default='reduce',
        type=str
    )
    return myParser.parse_args()

if __name__=="__main__":
    import argparse,time
    myParser=parser()
    tic=time.time()
    moviepyConcatVideos(myParser.input,myParser.output,myParser.method)
    toc=time.time()
    print(f'time taken to concat video clips -- {round(toc-tic)} secs')