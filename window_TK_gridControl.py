#window_TK_gridControl.py



from tkinter import *

#from tkmacosx import *


win = Tk()
win.title('First Application!')
l1=Label(win, text='Label 1', bg='lightblue', fg='blue')
l2=Label(win, text='Label 2', bg='lightblue', fg='blue')
l3=Label(win, text='Label 3', bg='lightblue', fg='blue')
l4=Label(win, text='Label 4', bg='lightblue', fg='blue')
l5=Label(win, text='Label 5', bg='lightblue', fg='blue')
l6=Label(win, text='Label 6', bg='lightblue', fg='blue')
l7=Label(win, text='Label 7', bg='lightblue', fg='blue')
l8=Label(win, text='Label 8', bg='lightblue', fg='blue')
l9=Label(win, text='Label 9', bg='lightblue', fg='blue')
l10=Label(win, text='Label 10', bg='pink', fg='red')

l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=0, column=1, padx=5, pady=5)
l3.grid(row=0, column=2, padx=5, pady=5)
l4.grid(row=1, column=0, padx=5, pady=5)
l5.grid(row=1, column=1, padx=5, pady=5)
l6.grid(row=1, column=2, padx=5, pady=5)
l7.grid(row=2, column=0, padx=5, pady=5)
l8.grid(row=2, column=1, padx=5, pady=5)
l9.grid(row=2, column=2, padx=5, pady=5)
l10.grid(row=3, columnspan=3, padx=5, pady=5)

win.mainloop()