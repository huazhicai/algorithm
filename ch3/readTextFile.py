#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter filename:')
print

# attempt to open file for reading
try:
	fobj = open(fname, 'r')
# except IOError, e:
except IOError as e:
	print("*** file open error:", e)
# if not os.path.exists(fname):
# 	print("ERROR: '%s' is not exists" % fname)
else:
	# display contents to the screen
	for eachLine in fobj:
		# print(eachLine, end='')
		print(eachLine.strip())
	fobj.close()