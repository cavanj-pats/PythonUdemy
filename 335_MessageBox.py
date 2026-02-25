#334_MenuWidget.py
"""
askokcancel, askquestion, askretrycancel, askyesnow
showerror, showinfo, showwarning

options:  default - ok, yes, retry
icon = ERROR, INFO, QUESTION, WARNING
parent - parent window
"""

import tkinter as tk
import tkinter.messagebox as msg

#from tkinter.font import *
#from tkmacosx import *

def myhandler():
    #ans = msg.askyesno('My message', 'Do you want to continue?')  #this works for Yes/No msg box
    ans = msg.askokcancel('My ask ok cxl', 'OK to launch missiles!', default='cancel', parent=win)  #by making parent win, box will disable app until result of dialog box. Dialog will pop up inside of win.
    #there is also an 'asquestion' dialog.  it's default will be yes/no not ok/cancel.
    print(ans)


win = tk.Tk()
win.title('First Menu Application!')
win.geometry('600x400')   #add +100+10 places the windowget()

btn1=tk.Button(win, text='Click Me', command=myhandler)
btn1.pack()


win.mainloop()