#333_stopwatch.py


from tkinter import *  # type: ignore
import time
import datetime

#from tkinter.font import *

#from tkmacosx import *

def update_time():
    global running, elapsed_time
    if running:
        elapsed_time += time.time()
        lbl1['text'] = ms.strftime('%M:%S:%f'[:-3])
        lbl1.after = (10, btnStart_Click())
       
  

def btnStart_Click():
    global running, elapsed_time, start_time
    running = True
    

    update_time()
        
        lbl1['text'] = ms.strftime('%M:%S:%f'[:-3])
        lbl1.after = (10, btnStart_Click())
    #stop when stop when stop is pushed
    #reset when reset is pushed

    
    




win = Tk()
win.title('Stop watch challenge Application!')
win.geometry('400x200')   #add +100+10 places the windowget()




#ff5555 would have red and some green and some blue.   RGB
lbl1 = Label(win, bg='red', font=('courier', 30 ), fg='yellow', text='00:00:000' )
#lbl1.pack(fill=BOTH, expand=True)  #not 'both' and not 1 vs BOTH and True
lbl1.grid(column=0,columnspan=3,row=0)  #grid column, columnspan row
#could not use textvariable with a var =StrValue()
#could not assign value to var in function.
btnStart = Button(win, text='Start', command=btnStart_Click)
btnStart.grid(column=0,columnspan=1,row=1)

btnStop = Button(win, text='Stop')
btnStop.grid(column=1,columnspan=1,row=1)

btnReset = Button(win, text='Reset')
btnReset.grid(column = 2,columnspan=1,row=1)






win.mainloop()