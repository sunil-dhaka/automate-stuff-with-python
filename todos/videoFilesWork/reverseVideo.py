'''
author: @sunil-dhaka
use: to reverse videos by extracting frames and loading them in the inverted order using MoviePy library in Python
'''

import datetime
import sys
import os
import shutil
import glob

from typing import Tuple
from moviepy.editor import VideoFileClip, ImageSequenceClip
import numpy as np

FPS_VALUE = 10


def reverseVideo(frames_path: str, video_fps: int, remove_frames: bool = True):
    '''
    reverse video file
    '''
    frame_files = glob.glob(os.path.join(frames_path, '*'))

    sorted_frame_files = sorted(frame_files, key=lambda frame_file: datetime.datetime.strptime(
        frame_file.split('_')[1], '%H-%M-%S.%f.jpg'), reverse=True)

    saving_fps = min(video_fps, FPS_VALUE)
    if saving_fps == 0:
        saving_fps = video_fps

    image_sequence_clip = ImageSequenceClip(sorted_frame_files, fps=saving_fps)

    out_file_name = frames_path+'_reversed.mp4'

    image_sequence_clip.write_videofile(out_file_name)

    if remove_frames:
        shutil.rmtree(frames_path)


def nameFrames(time_delta: str) -> str:
    try:
        main_time, milisecs = time_delta.split('.')
    except ValueError:
        return time_delta+'.00'

    milisecs = int(milisecs)
    milisecs = round(milisecs/1e4)

    # here :02 does the work of zfills(2)
    return f'{main_time}.{milisecs:02}'


def extrcatFrames(video_file: str) -> Tuple[str, int]:
    """
    extract video frames
    """

    video_file_name, _ = os.path.splitext(video_file)
    if not os.path.isdir(video_file_name):
        os.mkdir(video_file_name)

    video_clip = VideoFileClip(video_file)
    # set fps rate at which to capture images/frames
    capture_fps = min(video_clip.fps, FPS_VALUE)

    if capture_fps == 0:
        capture_step = 1/video_clip.fps
    else:
        capture_step = 1/capture_fps

    for current_duration in np.arange(0, video_clip.duration, capture_step):
        formatted_frame_timestamp = nameFrames(
            str(datetime.timedelta(seconds=current_duration))).replace(':', '-')
        frame_name = os.path.join(
            video_file_name, f'frame_{formatted_frame_timestamp}.jpg')
        video_clip.save_frame(frame_name, current_duration)

    return video_file_name, video_clip.fps


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please give video file that needs to reversed')
        sys.exit()
    video_file = sys.argv[1]

    frames_folder, video_fps = extrcatFrames(video_file)
    reverseVideo(frames_folder, video_fps)
