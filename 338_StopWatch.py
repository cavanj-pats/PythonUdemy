#333_stopwatch.py


from tkinter import *  # type: ignore
import time

#from tkinter.font import *

#from tkmacosx import *

class Stopwatch:
    def __init__(self):
        self._start_time=None
        self._elapsed_time = 0

    def start(self):
        if self._start_time is None:
            self._start_time = time.time()

    def stop(self):
        if self._start_time is not None:
            tp =  time.time() - self._start_time
            self._elapsed_time += tp
            self._start_time is None


    def reset(self):
        self._start_time = None
        self._elapsed_time = 0


    def get_elapsed_time(self):
        return self._elapsed_time

    def display_time(self):
        return time.ctime()
    

  

def btnStart_Click():
  # reset clock
  #start clock
  #run clock
    if not running:
        running = True
        sw.reset

    lbl1['text'] = sw.get_elapsed_time()
    lbl1.after = (10, btnStart_Click())
  #stop when stop when stop is pushed
  #reset when reset is pushed

    
    




win = Tk()
win.title('Stop watch challenge Application!')
win.geometry('400x200')   #add +100+10 places the windowget()


sw = Stopwatch()
running = False

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