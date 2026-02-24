#331_scale_slider.py


from tkinter import *  # type: ignore
#from tkinter.font import *

#from tkmacosx import *

def validateNotDigit(txt):
    if txt.isdigit():
        return False
    else:   
        return True

win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the window

#entry widget validatecommands require the function to be registered
#this is the registration 
handl=(win.register(validateNotDigit), '%S')   #%S is for new text entered or deleted.  this is a control character

var = StringVar(value='Hello World')   #show='*' makes it a password entry widget
ent1 = Entry(win, textvariable=var, validate='key', validatecommand=handl )
ent1.pack()
ent1.focus()
ent1.icursor(4)
ent1.select_to(10)   #can also select range
#ent1.insert
#ent1.delete(0,3)  #delete just these characters in teh entry box



win.mainloop()