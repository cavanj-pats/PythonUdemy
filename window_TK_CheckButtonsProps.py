

from tkinter import * # type: ignore
#from tkmacosx import *

def evt_handler():
    l1['text'] = cb1['text'] if var1.get() == 1 else  ''
    l1['text'] += cb2['text'] if var2.get() == 1 else  ''
    l1['text'] += cb3['text'] if var3.get() == 1 else  ''

#select() or toggle() will only check the cb1. it won't trigger the event
def btn1_handler():
    cb1.invoke()  # will invoke checking the checkbox toggle will behave like a cb1 check event, not just changing the check property
    cb2.invoke()
    cb3.invoke()


    
win = Tk()
win.title('First Application!')
win.geometry('600x400+100+10')   #+100+10 places the window
win.resizable(True, True)  #x and y 
#win.attributes('-alpha',0.55)   #-alpha, 0.25 made window transparent, can keep messing with the float value.  opaqueness level

#add a label
l1 = Label(win, text='')  # create a label reference the window it will be in
l1.pack()  #add label to the window

var1 = IntVar()
cb1 = Checkbutton(win, variable= var1, text='Java', command= evt_handler )
cb1.pack()

var2 = IntVar()
cb2 = Checkbutton(win, variable= var2, text='C++', command= evt_handler )
cb2.pack()

var3 = IntVar()
cb3 = Checkbutton(win, variable= var3, text='Python', command= evt_handler )
cb3.pack()

btn1 = Button(win, text='Click to Toggle', command=btn1_handler)
btn1.pack()

"""
v1='t'

r= Radiobutton(win, text='Option 1', variable=v1, value=1) # type: ignore
r.pack()
r2 = Radiobutton(win, text='Option 2', variable=v1, value=2) # type: ignore
r3 = Radiobutton(win, text='Option 3', variable=v1, value=3) # type: ignore
r2.pack()
r3.pack()

#option menu or listbox/combobox
v = StringVar()
opt=OptionMenu(win, v, 'Python', *('Java','C++', 'Javascript','Python'))
opt.pack()

#scale or slider or sliding bar
s = Scale(win, from_=0, to=100)
s.pack()

"""



win.mainloop()


