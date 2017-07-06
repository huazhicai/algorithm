#!/usr/bin/env python

import os
ls = os.linesep

# get filename
def writeFile():
   while True:
      fname = input("Please input filename:\n")
      if os.path.exists(fname):
         print("ERROR: '%s' already exists." % fname)
      else:
         break

   # get file content (text) lines
   all = []
   print("\nEnter lines ('.' by itself to quit).\n")

   # loop until user terminates input
   while True:
      entry = input('>')
      if entry == '.':
         break
      else:
         all.append(entry)

   # write lines to file with proper line-ending
   fobj = open(fname, 'w')
   fobj.writelines(['%s%s' % (x, ls) for x in all])
   fobj.close()
   print("Done!")


def readFile():
   fname = input("Enter filename:")
   print()
   # attempt to open file for reading
   try:
      fobj = open(fname, 'r')
   except IOError as e:
      print("*** file open error:", e)
   else:
      # display contents to the screen
      for eachLine in fobj:
         # print(eachLine, end='')
         print(eachLine.strip())
      fobj.close()


def editFile():
   while True:
      fname = input("Enter filename:")
      if not os.path.exists(fname):
         print("ERROR: '%s' not exists" % fname)
      else:
         try:
            # call sysem command to edit file content
            os.system('vim {}'.format(fname))
            print()
            print('{} has been changed'.format(fname))
            # break
         except IOError as e:
            print("ERROR:", e)


if __name__ == '__main__':
   while True:
      print('''
Input the function number:
1.MakeFile
2.ReadFile
3.EditFile
4.Exit
   ''')
      ch = int(input('Function:'))
      if ch == 1:
         writeFile()
      elif ch == 2:
         readFile()
      elif ch == 3:
         editFile()
      else:
         break