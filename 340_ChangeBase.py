#339_FontOptions


from tkinter import *  # type: ignore


#from tkinter.font import *

#from tkmacosx import *

def handler():
    global  lblVal
    if var1.get() == 1:
        lbl1['text'] = lblVal
    elif var1.get() == 2:
        lbl1.config(text=format(lblVal, 'b') )
    elif var1.get() == 3:
        lbl1['text']= format(lblVal, 'x')
    elif var1.get() == 4:
        lbl1['text'] = format(lblVal,'o').upper()



win = Tk()
win.title('Radio Button to Change Base')
win.geometry('400x300')   #add +100+10 places the windowget()

global lblVal
lblVal= 35

#ff5555 would have red and some green and some blue.   RGB
lbl1 = Label(win, bg='black', font=('Times New Roman', 45), fg='yellow', text=str(lblVal) )
#lbl1['font']=(Font(family = 'Times New Roman' , size = 45))
#lbl1.pack(fill=BOTH, expand=True)  #not 'both' and not 1 vs BOTH and True
lbl1.grid(column=0,columnspan=4,row=0)  #grid column, columnspan row


var1 = IntVar(value = 0)
rb1 = Radiobutton(win, text='Decimal', variable=var1, value=1, command=handler)
rb1.grid(column = 0, row=1)

rb2 = Radiobutton(win, text='Base 2', variable= var1, value=2, command=handler)
rb2.grid(column = 1, row=1)

rb3 = Radiobutton(win, text='Hex',variable= var1, value=3, command=handler)
rb3.grid(column = 2, row=1)

rb4 = Radiobutton(win, text='Oct', variable= var1, value=4,  command=handler)
rb4.grid(column = 3, row=1)

rb1.select()  #this selects decimal and shows the others in the off state versus minus sign.



win.mainloop()