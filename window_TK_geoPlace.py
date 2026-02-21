#window_TK_geoPlace.py


from tkinter import *

#from tkmacosx import *

win = Tk()
win.title('First Application!')
win.geometry('600x400+100+10')   #+100+10 places the window


b1 = Button(win, text="Click 1", bg='lightblue', fg='blue')
b2 = Button(win, text="Click 2", bg='lightblue', fg='blue')

b1.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.1)
b2.place(relx=0.5, rely=0.6, relwidth=0.15, relheight=0.1)



win.mainloop()