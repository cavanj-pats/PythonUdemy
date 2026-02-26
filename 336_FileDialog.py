#336_FileDialog
"""

"""

from tkinter import * # type: ignore
from tkinter.filedialog import * # type: ignore

#from tkinter.font import *
#from tkmacosx import *
def openhandler():
    #fname = askopenfilename()   #this is just the path and filename
    fname = askopenfile()   #reads the entire object
    txt = fname.read()   #read teh contents of the file
    txt1.insert('1.0', txt)

    #print(fname)

def savehandler():
    fname = asksaveasfile()
    fname.write(txt1.get('1.0', 'end-1c'))

def clearhandler():
    txt1.delete('1.0', 'end-1c')  #'end-1c' means last row and column

win = Tk()
win.geometry('600x400')   #add +100+10 places the windowget()

txt1 = Text(win, height=10)
txt1.pack()

btn1 = Button(win, text='Open', command=openhandler)
btn1.pack()

btn2 = Button(win, text='Save', command=savehandler)
btn2.pack()

btn3 = Button(win, text='Clear', command=clearhandler)
btn3.pack()


#fileOpen=fd.askopenfilename(win)



win.mainloop()