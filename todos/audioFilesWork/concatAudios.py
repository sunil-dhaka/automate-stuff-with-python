'''
author: @sunil-dhaka
todo: use tqdm to show fancy progress bar for file reading and concatening
added: automatically convert non-wav files into wav for wave method  << done
todo: add low quality options for wav conversion in toWAV()
'''
from moviepy.editor import concatenate_audioclips, AudioFileClip
import wave 
from pydub import AudioSegment
import os,subprocess

def toWAV(file):
    '''
    description:
        convert audio files into '.wav' files using ffmpeg unix utility

    input:
        file: input audio file
    '''
    
    if os.path.splitext(file)[1]!='.wav':
        base_path='/'.join(os.path.abspath(file).split('/')[:-1])
        wav_file=os.path.splitext(file)[0]+'.wav'
        new_file=os.path.join(base_path,wav_file)
        # to check whether wav version of mp3 exists or not if not only then convert to wave
        if not os.path.exists(new_file):
            subprocess.call(['ffmpeg','-i',file,'-vn', '-acodec','pcm_s16le', '-ac', '1', '-ar','44100', '-f', 'wav',new_file],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
            print('Converted to wav -- ',wav_file)
            # rename file to wav version using mv unix command
            # subprocess.call(['mv',file,new_file],stderr=subprocess.STDOUT,stdout=subprocess.DEVNULL)
            # print(f'Renamed: {file}\nto ----: {new_file}')

def moviepyConcatAudios(inputClips,outClipPath):
    '''
    using moviepy
    issue: some weird errors with MoviePy when reading some audio files.
    
    input:
        inputClips: input audio files
        outClipPath: output concated file path
    '''
    print('Using moviepy method.')
    audioFiles=[]
    for clip in inputClips:
        audioFiles.append(AudioFileClip(clip))

    concatFile=concatenate_audioclips(audioFiles)
    concatFile.write_audiofile(outClipPath)
    print('Concated and saved @', outClipPath)

def waveConcatAudios(inputClips,outClipPath):
    '''
    using wav
    issue: only works with .wav files
    This method is reliable and much faster. 
    However, the downside is that only the wav extension is supported
    sol: either convert input files into wav or use pydub method

    input:
        inputClips: input audio files
        outClipPath: output concated file path
    '''
    print('Using wave method.')
    for clip in inputClips:
        toWAV(clip)
    renamedInputClips=[]
    for clip in inputClips:
        base_path='/'.join(os.path.abspath(clip).split('/')[:-1])
        wav_clip=os.path.splitext(clip)[0]+'.wav'
        renamed_file=os.path.join(base_path,wav_clip)
        renamedInputClips.append(renamed_file)

    audioData=[]
    for clip in renamedInputClips:
        tmp_file=wave.open(clip,'rb')
        audioData.append([tmp_file.getparams(),tmp_file.readframes(tmp_file.getnframes())])
    
    # set params of outfile same as first clip file
    with wave.open(outClipPath,'wb') as outFile:
        outFile.setparams(audioData[0][0])
        for c in range(len(audioData)):
            outFile.writeframes(audioData[c][1])

    print('Concated and saved @', outClipPath)

def pydubConcatAudios(inputClips,outClipPath):
    '''
    using pydub
    preferred: use this method to combine several audio files into one,
    as it supports a lot of audio file extensions and does not 
    produce any weird error when loading audio files

    input:
        inputClips: input audio files
        outClipPath: output concated file path
    '''
    print('Using pydub method.')
    audioData=[]
    def getFileExt(file):
        return os.path.splitext(file)[1].lstrip('.')

    for clip in inputClips:
        clip_ext=getFileExt(clip)
        clip_data=AudioSegment.from_file(clip,clip_ext)
        audioData.append(clip_data)
    
    outClip=audioData[0]

    for c in range(1,len(inputClips)):
        outClip+=audioData[c]
    
    outClipExt=getFileExt(outClipPath)

    outClip.export(outClipPath,format=outClipExt)
    print('Concated and saved @', outClipPath)

def parser():
    myParser=argparse.ArgumentParser(description='script to concat multiple audio files into single file',prog='concatAudios',epilog='Useful script. author: @sunil-dhaka')
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
        help='input audio file names/paths'
    )
    myParser.add_argument(
        '-m',
        '--method',
        help='which method to use? moviepy | wave | pydub',
        default='pydub',
        type=str
    )
    return myParser.parse_args()

if __name__=="__main__":
    import argparse
    myParser=parser()
    methodUsed=myParser.method.lower()
    if methodUsed.startswith('w'):
        waveConcatAudios(myParser.input,myParser.output)
    elif methodUsed.startswith('m'):
        moviepyConcatAudios(myParser.input,myParser.output)
    else:
        pydubConcatAudios(myParser.input,myParser.output)
