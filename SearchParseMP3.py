#!/usr/bin/env python

#builtin modules
from sys import argv as arg
from subprocess import call
import glob
from os import system as cmd
import os.path
import fnmatch
import string
#import re
from shutil import copy2, move 
#mutagen modules
#import mutagen
from mutagen.mp3 import MP3 as mp3
from mutagen.mp4 import MP4 as mp4
from mutagen.flac import FLAC as flac
from mutagen.id3 import ID3, TIT2, TPE1, TALB

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

# for i in songlist:
# 	print ((i[1])[0])

#may be tricky to change code later if function only accepts select strings from specific list?
def mp3parse(listob):
	for song in sorted(listob):
		#modify indiced if just using a list
		if (song[1])[1]==".mp3":
			smp3=mp3(song[2])
			s=(song[1])[0]
			artist,album,title = (smp3.get('TPE1'),smp3.get('TALB'),smp3.get('TIT2'))
			# weeds out files with incomplete metadata
			if not title:
				#create function to assign metadata to file based info from filename
				#?move files to dir for orphaned or files with no metadata? 
		 		pass
		 		#print "no title metadata for: %s" % (song[1])[0]
			# elif not album:
			# 	#move file to orphaned file dir
			#  	continue
			elif not artist:
				#move file to orphaned file dir
				pass
			else:
			# 	#prints pretty formatted metadata of mp3 files (temporary. Just to see if working)
			# 	#yield "%s - %s - %s \n %s \n" % (artist,album,songname,s)
				yield artist,s


#generates list with tuple variables of artist and filepath
filepath=list(f.split(',') for f in (sorted(list((str(i[0])+","+i[1] for i in mp3parse(songlist))))))

# for i in songlist:
# 	print (i[1])[0]

# for i in mp3parse(songlist):
# 	print i 

def mkfolder(name=None):
	if name==None:
		pass
	elif fnmatch.fnmatch(name,'*\x00'):
		pass
	else:
		os.mkdir(name)



#make directories
for name in filepath:
	foldername=str(arg[2])+name[0]
	filename=str(arg[1])+name[1]
	try:
		mkfolder(foldername)
	except OSError:
		# print "%s \t\n exists!" % dirname
		pass
	#using builtin modules and calling external programs gives errors!!!
	sh="cp %s %s" % (foldername,filename)
	print sh
	cmd("cp %s %s" % (foldername,filename))  


#1. add parsing of flac and mp4 and other codecs to mp3parse function

#create artist name dir and album name subdir from metadata if more then one file found with matching id3 data

