 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
bfg=Button(root,text='change foreground',fg='red')
bfg.pack()
bbg=Button(root,text='change background',bg='blue')
bbg.pack()
root.mainloop()