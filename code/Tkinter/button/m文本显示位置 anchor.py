 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
for a in['n','s','e','w','ne','nw','se','sw']:
	Button(root,
	text='anchor',
	anchor=a,
	width=30,
	height=4).pack()
root.mainloop()