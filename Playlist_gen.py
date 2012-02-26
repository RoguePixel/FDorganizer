#!/usr/bin/env python
from sys import argv as arg
import glob
import os
import os.path
import fnmatch


cwd=os.getcwd()
aformats=('*.mp3','*.aac','*.flac','*.wav','*.m4a')
playlist=open('playlist.m3u','a')
home=os.getenv('HOME')
fdir=' '.join(arg[1:])
#musicdir=' '.join(arg[1:])
#os.path.splitext(os.path.join(path,name))


def listaudiofiles(root=os.getcwd()):
    for path, dirs, files in os.walk(root):
		for name in files:
			yield os.path.abspath(os.path.join(path,name))


if len(arg)==1:
	#fdir=cwd
	#print "print searching for audio in %s" % cwd
	print "specify directory"

if not os.path.isdir(fdir):
	print "\nno directory exits!"
else:
	playlistname=raw_input("\nname for playlist? (defualt is playlist)\n")

#choose to name resulting playlist file
	if not playlistname:
		pass
	else:
		playlist=open(playlistname+".m3u",'a')


for f in listaudiofiles(fdir):
	ext=os.path.splitext(f)
	for format in aformats:
		if "*"+ext[1]==format:
			f=str(f)
			#print f#, ext[1]
			playlist.write("%s\n" % f)

playlist.close




