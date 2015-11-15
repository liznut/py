 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
for b in[0,1,2,3,4]:
	Button(root,
	text= string(b),
	bd=b).pack()
root.mainloop()