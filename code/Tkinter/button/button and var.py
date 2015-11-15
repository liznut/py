 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
def changeText():
	if b['text']=='text':
		v.set('change')
		print'change'
	else:
		v.set('text')
		print'text'
v=StringVar()
b=Button(root,textvariable=v,command=changeText)
v.set('text')
b.pack()
root.mainloop()
#将变量v与Button绑定，当v值变化时，Button显示的文本也随之变化