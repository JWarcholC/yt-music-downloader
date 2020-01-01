#!/usr/bin/python3

from __future__ import absolute_import, unicode_literals
import os
import sys
import youtube_dl

# prepare cleaning instruction
clean = ""
if os.system == "Windows":
    clean = "cls"
else:
    clean = "clear"


# progress bar
def hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')


def file_len(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    try:
        return i + 1
    except UnboundLocalError as err: 
        print('File {0} is empty!'.format(file_name))
        exit(-1)


def start(url):
    with youtube_dl.YoutubeDL(opts_d) as yt:
        yt.download([url])


def file_reader(file):
    with open(file, "r") as f:
        ln = file_len(file)
        i = 0
        for url in f:
            os.system(clean)
            print('It remains {0} from {1}'.format(ln - i, ln))
            i = i + 1
            start(url)


def help():
    print('Usage: ytdown (-d [DIRECTORY]) [FILE_WITH_LIST]')
    print('-h: print help') 


# configuration dictionary
opts_d = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'outtmpl': '%(title)s'+'.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [hook],
    'forcetitle': True,
    'quiet': False,
}


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 4:
        help()
        exit(-1)
        
    else: # if You could download more clips
        if sys.argv[1] == '-h':
            help()
            exit(0)
            
        if sys.argv[1] == '-d': 
            os.chdir(sys.argv[2]) # change directory 
            path = sys.argv[3] # assign path to list
        
        else: # path to file with youtube link list
            path = sys.argv[2]
        
        file_reader(path) # read file
        exit(0)
    
    start(sys.argv[1]) # if any addictional arguments
    exit(0)


if __name__ == "__main__":
    main()
