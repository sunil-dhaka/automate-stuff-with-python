"""
author: @sunil-dhaka
script to trip/crop audio file at given points
TODO: pydub.exceptions.CouldntDecodeError: Couldn't find fmt header in wav data
"""
import argparse
import os
from pydub import AudioSegment

def cropAudio(file_path:str,start_cut_point:str,end_cut_point:str):
    # convert time points into milisecs
    try:
        start_hour,start_min,start_sec=start_cut_point.split(':')
        start_milisec=(int(start_hour)*3600+int(start_min)*60+int(start_sec))*1000

        end_hour,end_min,end_sec=end_cut_point.split(':')
        end_milisec=(int(end_hour)*3600+int(end_min)*60+int(end_sec))*1000

    except ValueError:
        start_min,start_sec=start_cut_point.split(':')
        start_milisec=(int(start_min)*60+int(start_sec))*1000

        end_min,end_sec=end_cut_point.split(':')
        end_milisec=(int(end_min)*60+int(end_sec))*1000

    split_path=os.path.abspath(file_path).split('/')
    base_dir='/'.join(split_path[:-1])
    file_name=split_path[-1].split('.')[0]
    file_ext=split_path[-1].split('.')[1]

    audio_file=AudioSegment(file_path)
    sound_clip=audio_file[start_milisec:end_milisec]

    sound_clip.export(os.path.join(base_dir,f'{file_name}_{start_milisec}:{end_milisec}.{file_ext}'),format=file_ext)

def parser():
    input_parser=argparse.ArgumentParser(
        prog='cropAudio',
        description='script to trip/crop audio file at given points',
        epilog='author: @sunil-dhaka'
    )
    input_parser.add_argument(
        '-i',
        '--input',
        required=True,
        help='input audio file'
    )
    input_parser.add_argument(
        '-s',
        '--split',
        required=True,
        nargs='+',
        help='format of input is 1:20(1 min 20 sec)'
    )
    return input_parser.parse_args()

if __name__=="__main__":
    my_parser=parser()
    cropAudio(my_parser.input,my_parser.split[0],my_parser.split[1])