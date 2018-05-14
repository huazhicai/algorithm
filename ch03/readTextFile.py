#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter file name: ')
print()  # 隔一行

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as err:
    print("*** file open error:", err)
# 如果没有异常发生，则执行这段代码
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine, end='')  # 去行
    fobj.close()