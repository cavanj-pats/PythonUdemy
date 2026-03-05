#346_FrameAndLabelFrame.py


from tkinter import *




win = Tk()
win.geometry('600x400')
win.title('346 Frame and Label Frame')

f1 = LabelFrame(win, bg='red',text='Frame 1', width=300)
f1.pack(side=LEFT, fill=Y)

f2 = LabelFrame(win, bg='green',text=' Frame 2', width=300)
f2.pack(side=RIGHT, fill=Y)

b1 = Button(f1, text='Button 1')
b2 = Button(f1, text='Button 2')
b3 = Button(f1, text='Button 3')
b4 = Button(f1, text='Button 4')
b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=0, row=1)
b4.grid(column=1,row=1)


b11 = Button(f2, text='Button 11')
b12 = Button(f2, text='Button 12')
b13 = Button(f2, text='Button 13')
b14 = Button(f2, text='Button 14')
b11.grid(column=0, row=0)
b12.grid(column=1, row=0)
b13.grid(column=0, row=1)
b14.grid(column=1,row=1)



win.mainloop()

