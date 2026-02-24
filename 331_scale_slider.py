#331_scale_slider.py


from tkinter import *  # type: ignore
from tkinter.font import *

#from tkmacosx import *

def myhandler(e):
    f = Font(size=str(scl1.get()))
    ent1['font']=f

win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

var = StringVar(value='Hello World')
ent1 = Entry(win, textvariable=var)
ent1.pack()

#for Scale when providing a command= function,  the handler function needs to reference
#the event myhanlder(e).  e for event.
scl1 = Scale(win, from_=10, to=30, tickinterval=4, resolution=4, command=myhandler)
scl1.pack()


win.mainloop()