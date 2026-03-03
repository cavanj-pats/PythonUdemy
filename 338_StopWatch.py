#333_stopwatch.py


from tkinter import *  # type: ignore
import time
import datetime

#from tkinter.font import *

#from tkmacosx import *

def update_time():
    global flag, elapse_time
    if flag == True:
        elapse_time += 10
        milli = elapse_time % 1000
        sec = elapse_time // 1000
        min = sec // 60
        sec = sec % 60

        lbl1['text'] = f'{min:02d}:{sec:02d}:{milli:03d}'
        lbl1.after(10, update_time)
       
  

def btnStart_Click():
    global flag, elapse_time
    flag = True
    
    update_time()
      

def stop():
    global flag
    flag = False

def reset():
    global elapse_time, flag
    elapse_time=0
    flag = False
    lbl1['text']='00:00:000'
    
    




win = Tk()
win.title('Stop watch challenge Application!')
win.geometry('400x200')   #add +100+10 places the windowget()


global elapse_time
elapse_time = 0

#ff5555 would have red and some green and some blue.   RGB
lbl1 = Label(win, bg='red', font=('courier', 30 ), fg='yellow', text='00:00:000' )
#lbl1.pack(fill=BOTH, expand=True)  #not 'both' and not 1 vs BOTH and True
lbl1.grid(column=0,columnspan=3,row=0)  #grid column, columnspan row
#could not use textvariable with a var =StrValue()
#could not assign value to var in function.
btnStart = Button(win, text='Start', command=btnStart_Click)
btnStart.grid(column=0,columnspan=1,row=1)

btnStop = Button(win, text='Stop', command=stop)
btnStop.grid(column=1,columnspan=1,row=1)

btnReset = Button(win, text='Reset', command=reset)
btnReset.grid(column = 2,columnspan=1,row=1)






win.mainloop()