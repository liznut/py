 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
e=StringVar()
entry=Entry(root,textvariable=e)
e.set('input your text here')
entry.pack()
entry['state']='readonly'
root.mainloop()
#stete can also be bormal,active,disabled=readonly