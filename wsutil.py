# -*- coding: cp1251 -*-

from Tkinter import *

def button_clicked():
    print (u"Клик!")
    
root=Tk()
root.title('wsutil')

Button(root, text = u'Стрип', command = button_clicked).place(x = 20, y = 10, width = 70)
Button(root, text = u'Деять', command = button_clicked).place(x = 100, y = 10, width = 70)
Button(root, text = u'Перенос', command = button_clicked).place(x = 20, y = 50, width = 70)
Button(root, text = u'Перенос2', command = button_clicked).place(x = 100, y = 50, width = 70)
Button(root, text = u'Деразрядка', command = button_clicked).place(x = 50, y = 90, width = 100)

root.mainloop()
