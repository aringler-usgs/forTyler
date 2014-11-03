#!/usr/bin/env python


#Import a module to glob files together
import glob



#Wild card our files into a list
files = glob.glob('/xs0/seed/IU_ANMO/2014/2014_001*/*.seed')

#print the files we have to the screen
print(files)

#Or we can check the size of each file

#First we import the operating system
import os

#So for each file in our list we loop through
for curfile in files:
	#We calculate the size by getting the stats of the file from the os module
	#That is os.stat(curfile)

	#We then get the property of its size using .st_size
	#Finally we convert the integer to a string and print it
	print 'Here is the size of the file: ' + str(os.stat(curfile).st_size) + ' bytes'


#We could have also added the size of the files together 
filesizesum = 0

for curfile in files:
	filesizesum += os.stat(curfile).st_size


print 'Here is the size of all of the files: ' + str(filesizesum) + ' in bytes'

#We can also get the average by dividing by the number of files
#Notice I switched these numbers to floats instead of ints to do the division and then converted them to a string
print 'Here is the average file size: ' + str(float(filesizesum)/float(len(files))) + '  bytes'


