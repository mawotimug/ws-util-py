# -*- coding: cp1251 -*-

from Tkinter import *

def button_clicked():
    print (u"����!")
    
root=Tk()
root.title('wsutil')

Button(root, text = u'�����', command = button_clicked).place(x = 20, y = 10, width = 70)
Button(root, text = u'�����', command = button_clicked).place(x = 100, y = 10, width = 70)
Button(root, text = u'�������', command = button_clicked).place(x = 20, y = 50, width = 70)
Button(root, text = u'�������2', command = button_clicked).place(x = 100, y = 50, width = 70)
Button(root, text = u'����������', command = button_clicked).place(x = 50, y = 90, width = 100)

root.mainloop()
