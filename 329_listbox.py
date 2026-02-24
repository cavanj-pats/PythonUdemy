#329_listbox.py


from tkinter import *  # type: ignore
from tkinter.font import *

#from tkmacosx import *

def myhandler():
    var.set(lst1.curselection())

def on_double_click(e):
    myhandler()

win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

var = StringVar()
ent1 = Entry(win, textvariable=var)
ent1.pack()


lst1 = Listbox(win, selectmode=EXTENDED)
lst1.insert(0, 'Python')
lst1.insert(1, 'Java')
lst1.insert(2, 'C++')
lst1.insert(3, 'JavaScript')
lst1.insert(4, 'Ruby')
lst1.insert(5, 'C Lang')
lst1.insert(6, 'PHP')
lst1.insert(7, 'C#')
lst1.insert(8, 'R')
lst1.insert(9, 'Swift')
lst1.insert(10, 'Android')
lst1.insert(11, 'VB')
lst1.insert(12, 'PERL')
lst1.insert(13, 'Kotlin')
lst1.insert(14, 'Go')
lst1.insert(15, 'Scala')

lst1.pack()

btn1 = Button(win, text='Click Here', command=myhandler)
lst1.bind("<Double-1>", on_double_click)
lst1.bind("<<ListboxSelect>>", on_double_click)


btn1.pack()



win.mainloop()