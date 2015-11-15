# -*- coding:utf-8 -*-

#完成一个极简交互式日记系统,需求如下:#
#一次接收输入一行日记#
#保存为本地文件#
#再次运行系统时,能打印出过往的所有日记#

def init():
	import sys

	diary = 'this is week1 task of diary\n '

	f = file('diary.txt','w') # open for 'w'riting
	f.write(diary) # write text to file
	f.close() # close the file

def write():
	diaryfile = 'diary.txt'

	while True:
		d = raw_input('diary:')
		if d == '':
			break
		else :
			f = open(diaryfile,'a')
			f.write(d)
			f.write('\n')
	f.close()

def read():
	f = file('diary.txt')

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
	f.close()

#	f=file(diaryfile)
#	store = p.load(f)


 