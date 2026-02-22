#window_TK_geoPlace.py

from tkinter import * # type: ignore
from tkinter.messagebox import * # type: ignore
#from tkmacosx import *

def fun(e):
    #print(f'Event is Generated. {e.widget} clicked')
    #the e is for the event
    msg=f'{e.widget} {e.type}'
    showinfo('Status', msg )

def on_enter_pressed(e):
    #enteredText = e1.get() + ' ' + e
    print(e)
    #e1['text']=''



win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

"""
b1 = Button(win, text="Click 1", bg='lightblue', fg='blue', command= lambda: fun('Button 1 clicked.'))
b2 = Button(win, text="Click 2", bg='lightblue', fg='blue', command= lambda: fun('Button 2 Clicked.'))

b1.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.1)
b2.place(relx=0.5, rely=0.6, relwidth=0.15, relheight=0.1)
"""
e1=Entry(win, bg='red', fg='yellow')
e1.place(x=100, y=100, width=350, height=100)

e1.bind('<Shift - Button>', fun)   #shift is a modifier  gotta hold shift and click
e1.bind('<KeyPress>', on_enter_pressed, add='+')  #add='+' for more than one function for a widget. for each subsequent event add this.

#win.bind_class('Entry', '<Button-1>',fun)  #this binds an entire class of control
#win.bind_all('<Button-1>', fun)  #this binds the  application.
#<Return>  there are numerous events to bind

win.mainloop()