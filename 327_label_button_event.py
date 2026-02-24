#327_label_button_event.py


from tkinter import *  # type: ignore
from tkinter.font import *

#from tkmacosx import *


def btn1_click():
   l1_var.set(l1_var.get() + 1)

   #the below WORKED fine.  Before I used l1_var I had no textvariable
   #just text. above seems it is the preferred method though

   #var = int(l1['text'])
   #var += 1
   #l1['text']= var


win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

fnt = Font(family='Coutier', size=30)

#take focus=0 does not allow keyboard focus.  tab and spacebar
b1 = Button(win, font=fnt, text='Click to Count', command= btn1_click)
b1.pack()

l1_var = IntVar(value = 0)
l1 = Label(win, text= 0, textvariable=l1_var, font=fnt)  #dont' need text=0 any longer
l1.pack()

win.mainloop()