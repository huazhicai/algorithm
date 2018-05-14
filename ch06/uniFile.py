#!/usr/bin/env python
'''
An example of reading and writing Unicode strings: Writes
a Unicode string to a file in utf-8 and reads it back in.
'''
CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = "你好世界！\n"
bytes_out = hello_out.encode(CODEC)   # 二进制字符
fobj = open(FILE, 'wb')
fobj.write(bytes_out)
fobj.close()

fobj = open(FILE, 'rb')
bytes_in = fobj.read()
fobj.close()
hello_in = bytes_in.decode(CODEC)   # 解码二进制
print(hello_in, end='')
