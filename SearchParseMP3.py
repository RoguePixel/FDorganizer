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


#may be tricky to change code later if function only accepts select strings from specific list?

def mp3parse(listob):
	for song in sorted(listob):
		#modify indiced if just using a list
		if (song[1])[1]==".mp3":
			smp3=mp3(song[2])
			s=song[2]
			artist,album,title = (smp3.get('TPE1'),smp3.get('TALB'),smp3.get('TIT2'))
			#weeds out files with incomplete metadata
			if not title:
				#create function to assign metadata to file based info from filename
				#?move files to dir for orphaned or files with no metadata? 
		 		pass
		 		#print "no title metadata for: %s" % (song[1])[0]
			elif not album:
				#move file to orphaned file dir
				pass
			elif not artist:
				#move file to orphaned file dir
				pass
			else:
				#prints pretty formatted metadata of mp3 files (temporary. Just to see if working)
				#yield "%s - %s - %s \n %s \n" % (artist,album,songname,s)
				yield artist

artistlist=list(i for i in mp3parse(songlist))

#list is in unicode format!! List cannot be sorted unless formatted!!

#alistformatted=sorted(artistlist) #<<<< doesn't work!

print str(alistformatted)

#testing to see if printed strings are in alphabetical order
# n=0
# for i in alistformatted:
# 	n+=1
#  	print n,i 

#NEED SOME METHOD OF COMPARING ITEMS IN LIST 

# for i in range(1,len(artistlist)):
# 	for s in artistlist[i]:
# 		if s==artistlist[i]:
# 			print i,s

#print(len(artistlist))

#TODO
#1.make dir of artist name 
#2.compare names from list 
#3.count comparison 
#4.if less then 2 match delete	

#1. add parsing of flac and mp4 and other codecs to mp3parse function

#create artist name dir and album name subdir from metadata if more then one file found with matching id3 data

