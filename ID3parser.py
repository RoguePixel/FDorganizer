#!/usr/bin/env python

"""
usage: 

fdorg.py [flags] [PATH/TO/UNORGANIZED/DIRECTORY] [PATH/TO/DESTINATION/FOLDER]

possible flags?:

  -v Increase verbosity
  -m Only mp3
  -f Only FLAC
  -d Delete original files
  -t Test
  -w Sort files within the same folder they are originally in

mutagen:

import mutagen.[format]
metadata = mutagen.[format].Open(filename)

useful info:

TPE1 = artist
TIT2 = song
TALB = album

"""

from sys import argv as arg
from mutagen.mp3 import MP3 as mp3
from mutagen.mp4 import MP4 as mp4
from mutagen.flac import FLAC as flac
from mutagen.id3 import ID3, TIT2, TPE1, TALB
from os import system as do


#This function should be the main operation in sorting the files
#This doesn't do anything yet, just test runs the script with and without the 'v' flag
def metadata(path,dest):
    if 'v' in flag():
        do('ls ' + str(path))
    do('mkdir ' + str(dest) + '/test')

#Checks what flag was used 
def flag():
    opt = str(arg[1])
    return opt[1]

#Checks if a flag was used
def checkflag():
    if '-' in arg[1]:
        x = 'y'
    else:
        x = 'n'
    return x

#Test/ show all metadata for a specified file
#usage: fdorg.py -t /path/to/file/
try:
    if arg[1] == '-t':
        x = mp3(arg[2])
        print x.get('TPE1') #This shows the artist of the specified file
        print x.get('TALB') #This shows the album of the specified file
        exit()
except IndexError:
    pass
#/Test

#Shows usage of fdorg.py if wrong number of arguments are given
if len(arg) < 3 or len(arg) > 4:
    print "usage: fdorg.py [OPTIONS] [/directory/to/sort] [/destination/folder]"
    exit()

#Runs fdorg.py assuming no flags
if checkflag() == 'n':
    metadata(arg[1],arg[2])

#Runs fdorg.py with specified flags
if checkflag() == 'y':
    metadata(arg[2],arg[3])