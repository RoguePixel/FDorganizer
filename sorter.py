#!/usr/bin/env python

from sys import argv as arg
import glob
import os
import os.path
import fnmatch

cwd=os.getcwd()
home=os.getenv('HOME')

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
					yield path,ext

songlist=list(f for f in listaudiofiles(arg[1]))

# #print values of list
# for i in sorted(songlist):
# 	#stitches file path back together
# 	print os.path.abspath(os.path.join(i[0],(i[1])[0]))+(i[1])[1]
	

#NEED OPERATION TO MATCH NAMES FOR EACH NAME IN LIST AND MAKE DIRECTORY WITH NAMES THAT HAVE FOUND MATCHES!!


#BELLOW IS JUNK CODE \/

# n=0
# for song in sorted(songlist):
# 	title=(song[1])[0].lower().split(' ')
# 	for word in title: 
# 		print ' '.join(title)
	#print title
		# n=+1
		# if i in title[n]:
		# 	print ' '.join(title)	 
		# if i==(name for name in title):
		# 	print name


	# for i in title:
	# 	if "digitalism" in i:
	# 		print title

	#print titles[:-1],len(titles)-1
	# for t in titles:
	# 	print t
