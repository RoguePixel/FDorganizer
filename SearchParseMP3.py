#!/usr/bin/env python

#builtin modules
from sys import argv as arg
from os import system
import glob
import os
import os.path
import fnmatch
#mutagen modules
#import mutagen
from mutagen.mp3 import MP3 as mp3
from mutagen.mp4 import MP4 as mp4
from mutagen.flac import FLAC as flac
from mutagen.id3 import ID3, TIT2, TPE1, TALB

# cwd=os.getcwd()
# home=os.getenv('HOME')

#search for music of various formats and outputs ['path', 'filename','ext']
def listaudiofiles(root=os.getcwd()):
    for path, dirs, files in os.walk(root):
		for name in files:
			ext=os.path.splitext(name)
			#add or remove formats as needed
			#unused formats: ,'*.wav'
			for format in ('*.mp3','*.aac','*.flac','*.m4a'):
				if "*"+ext[1]==format:
					#yield os.path.abspath(os.path.join(path,name))
					yield path,ext,os.path.abspath(os.path.join(path,name))

#generates operable list of unformatted string data from listaudofiles
songlist=list(f for f in listaudiofiles(arg[1]))
#compiles list of filepaths from songlist
songlistformatted=list(song[2] for song in sorted(songlist))

#may be tricky to change code later if function only accepts select strings from specific list?
for song in songlist:
	if (song[1])[1]==".mp3":
		#print song[2]
		##had to check if file path string was true
		#print os.path.isfile(i) 
		x=mp3(song[2])
		if not x.get('TIT2'):
			#create function to assign metadata to file based info from filename
	 		print "no title metadata for: %s" % (song[1])[0]
		else:
			#prints pretty formatted metadata of mp3 files (temporary. Just to see if working)
			artist,album,songname = (x.get('TPE1'),x.get('TALB'),x.get('TIT2'))
			print "%s - %s - %s" % (artist,album,songname)

#create artist name dir and album name subdir from metadata if more then one file found with matching id3 data

