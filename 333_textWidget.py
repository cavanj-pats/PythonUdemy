#333_textWidget.py


from tkinter import *  # type: ignore
#from tkinter.font import *

#from tkmacosx import *

def myhandler1():
    txt1.edit_undo()

def myhandler2():
    txt1.edit_redo()

def printRange():
    print(txt1.get(0.1, 2.2))


win = Tk()
win.title('First Application!')
win.geometry('600x400')   #add +100+10 places the windowget()

#scroll bars require this weird linking between each of the objects it will be linked with
sc1 = Scrollbar(win, orient=VERTICAL)
sc1.pack(side=RIGHT, fill=Y)   #this is placement of the scrollbar

txt1 = Text(win, undo=True, yscrollcommand=sc1.set)
txt1.pack(side=LEFT)



#get() insert() and delete require a line number and index in that line   5.4 line 5 index 4 

sc1['command']=txt1.yview    #this is the end of the linking   you need to put it here after both objects are defined

btn1=Button(win, text='Click to Undo', command=myhandler1)
btn1.pack()

btn2=Button(win, text='Redo', command=myhandler2)
btn2.pack()

btn3=Button(win, text='Print', command=printRange)
btn3.pack()



win.mainloop()