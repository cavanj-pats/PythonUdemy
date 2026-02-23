

from tkinter import * # type: ignore
#from tkmacosx import *

def evt_handler():
    l1['text']=var.get()
  


    
win = Tk()
win.title('First Application!')
win.geometry('600x400+100+10')   #+100+10 places the window
win.resizable(True, True)  #x and y 
#win.attributes('-alpha',0.55)   #-alpha, 0.25 made window transparent, can keep messing with the float value.  opaqueness level

#add a label
l1 = Label(win, text='')  # create a label reference the window it will be in
l1.pack()  #add label to the window

var = StringVar()
rb1 = Radiobutton(win, variable= var, text='Java', value='Java', command= evt_handler )
rb1.pack()


rb2 = Radiobutton(win, variable= var, text='C++', value='C++', command= evt_handler )
rb2.pack()


rb3 = Radiobutton(win, variable= var, text='Python', value='Python', command= evt_handler )
rb3.pack()





win.mainloop()


