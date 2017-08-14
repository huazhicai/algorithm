#!/usr/bin/env python

import os
ls = os.linesep

# get filename
def writeFile():
   while True:
      fname = input("Please input file name:\n")
      if os.path.exists(fname):
         print("ERROR: '%s' already exists" % fname)
      else:
         break
   #get file content (text) lines
   all = []
   print("\nEnter lines ('.' by itself to quite).\n")

   #loop until user terminates input
   while True:
      entry = input('>>>')
      if entry == '.':
         break
      else:
         all.append(entry)
   #write lines to file with proper line-ending
   fobj = open(fname, 'w')
   fobj.writelines(['%s%s' %(x, ls) for x in all])
   fobj.close()
   print('Done!')


def readFile():
   fname = input("Enter filename: ")
   print
   # attempt to open file for reading
   try:
      fobj = open(fname,'r')
   except IOError as e:
      print(" *** file open error:", e)
   else:
      # display contents to the screen
      for eachLine in fobj:
         print(eachLine.strip())
      fobj.close()


if __name__ == '__main__':
	while True:
		print('''
Input the function number:
1.MakeFile
2.ReadFile
3.Exit
			''')
		ch = int(input('function:'))
		if ch == 1:
			writeFile()
		elif ch == 2:
			readFile()
		else:
			break