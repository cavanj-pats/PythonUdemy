#329_listbox.py


from tkinter import *  # type: ignore
from tkinter.font import *

#from tkmacosx import *

def myhandler():
    var.set(sb1.get())

win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

var = StringVar()
ent1 = Entry(win, textvariable=var)
ent1.pack()

"""
   spinbox can use from_  and to and increment for a range of numbers
   selection('to', 7). #deals with the selection
   selection('range', 1, 3)

   selection.get()
"""
items = ['Amazon', 'Ebay', 'Big-Y']

sb1 = Spinbox(win, values=items)


sb1.pack()



btn1 = Button(win, text='Click Here', command=myhandler)
btn1.pack()



win.mainloop()