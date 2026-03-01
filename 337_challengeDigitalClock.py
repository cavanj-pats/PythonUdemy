#333_textWidget.py


from tkinter import *  # type: ignore
import time

#from tkinter.font import *

#from tkmacosx import *

def myclock():
    str_time = time.strftime('%H:%M:%S') #%I would be 12 hour clock
    lbl1['text'] = str_time
    lbl1.after(100, myclock)



win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the windowget()

#ff5555 would have red and some green and some blue.   RGB
lbl1 = Label(win, bg='red', font=('courier', 40 ), fg='yellow' )
lbl1.pack(fill=BOTH, expand=True)  #not 'both' and not 1 vs BOTH and True

#could not use textvariable with a var =StrValue()
#could not assign value to var in function.


myclock()




win.mainloop()