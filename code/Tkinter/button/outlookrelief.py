 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
for r in['raised','sunken','groove','ridge']:
	Button(root,
	text=r,
	relief=r,
	width=30).pack()
root.mainloop()