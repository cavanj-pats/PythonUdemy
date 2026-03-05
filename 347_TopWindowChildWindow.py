#346_FrameAndLabelFrame.py


from tkinter import * # pyright: ignore[reportWildcardImportFromLibrary]
from tkinter.messagebox import * # pyright: ignore[reportWildcardImportFromLibrary]


class MyTop(Toplevel):
    def childhandler(self):
        showinfo('My', 'Child Window from Class Message')
    
    def __init__(self):
        Toplevel.__init__(self)
        bt = Button(self, text='Button 2', command=self.childhandler)
        bt.pack()

        #can also use a for loop to create mulitple buttons
        #there will be no variable name.  Text is linked to the index value of the loop
        



def myhandler():
    def childhandler():
        showinfo('My', 'Child window Message')
    
    tp1 = Toplevel(win)
    tp1.geometry('300x300')
    tp1.title('Child Window')

    bt = Button(tp1, text='Button 1', command=childhandler)
    bt.pack()
    tp1.mainloop()

def classhandler():
    tp2 = MyTop()
    tp2.geometry('250x250')
    tp2.title('Child Window from Class')
    tp2.mainloop()


win = Tk()
win.geometry('600x400')
win.title('347 Top Level and Child Window')


btn1 = Button(win, text='Click Me', command=myhandler)
btn1.pack()

btn2 = Button(win, text='Use Class for Child', command=classhandler)
btn2.pack()







win.mainloop()

