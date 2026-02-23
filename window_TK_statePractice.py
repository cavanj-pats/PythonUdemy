#window_TK_statePractice.py

from tkinter import * # type: ignore
from tkinter.messagebox import * # type: ignore
#from tkmacosx import *

"""
def fun(e):
    #print(f'Event is Generated. {e.widget} clicked')
    #the e is for the event
    msg=f'{e.widget} {e.type}'
    showinfo('Status', msg )

def on_enter_pressed(e):
    #enteredText = e1.get() + ' ' + e
    print(e)
    #e1['text']=''

"""
def fun(msg):
    l1['text']= msg


win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

#the highlight colors worked fine for an Entry widget but not for button
b1 = Button(win, text='Button 1', highlightbackground='red', highlightthickness=3, highlightcolor='yellow', command= lambda: fun('Button 1 Clicked.'))

b1.pack()

#take focus=0 does not allow keyboard focus.  tab and spacebar
b2 = Button(win, text='Button 2', command= lambda: fun('Button 2 Clicked.'))
b2.pack()


l1 = Label(win, anchor='s')
l1.pack()

win.mainloop()