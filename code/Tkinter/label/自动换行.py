 # -*- coding: utf-8 -*-
from Tkinter import*
root=Tk()
#Label(root,bg='welcome to jcodeer.cublog.cn',width=10,height=3).pack()
#左对齐，文本居中#
Label(root,text='welcome to jcodeer.cublog.cn',bg='yellow',width=40,height=3,wraplength=80,justify='left').pack()
#居中对齐，文本居左#
Label(root,text='welcome to jcodeer.cublog.cn',bg='red',width=40,height=3,wraplength=80,anchor='w').pack()
#居中对齐，文本居右#
Label(root,text='welcome to jcodeer.cublog.cn',bg='blue',width=40,heiht=3,wraplength=80,anchor='e').pack()

root.mainloop()

