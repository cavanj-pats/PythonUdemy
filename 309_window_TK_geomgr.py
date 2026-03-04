#window_TK_geomgr.py


from tkinter import * # type: ignore
#from tkmacosx import *


win = Tk()
win.title('First Application!')
#win.geometry('600x400+100+10')   #+100+10 places the window
win.resizable(True, True)  #x and y 
l1 = Label(win, text='Label 1', bg='red', fg='yellow')
#l1.pack(side=LEFT)   #places on left
#l1.pack()  #padx, pady add external gap outside the widget. ipadx, ipady adds gap between text and border of widget
l1.pack(side=LEFT, fill=Y, padx=2, pady=2, ipadx=5, ipady=5)

l2 = Label(win, text='Label 2', bg='red', fg='yellow')
#l2.pack(side=TOP)   #places at top
#l2.pack()
l2.pack(side=TOP, fill=X, padx=2, pady=2, ipadx=5, ipady=5)

l3 = Label(win, text='Label 3', bg='red', fg='yellow')
#l3.pack(side=RIGHT)  #places on right
l3.pack(side=LEFT, padx=2, pady=2, ipadx=5, ipady=5)

l4 = Label(win, text='Label 4', bg='red', fg='yellow')
#l4.pack(side=RIGHT)  #places on right
l4.pack(side=LEFT, padx=2, pady=2, ipadx=5, ipady=5)


#with anchor the controls are placed in order and achored to their spot in order
#but, there is a vertical order to them.  Each control on its own row


win.mainloop()