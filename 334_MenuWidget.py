#334_MenuWidget.py


from tkinter import *  # type: ignore
#from tkinter.font import *

#from tkmacosx import *




win = Tk()
win.title('First Menu Application!')
win.geometry('600x400')   #add +100+10 places the windowget()

def myhandler():
    txt1.insert(1.0, 'Hello World')  #insert line 1 before character 0.  this is the first character

def close_window(root_window):
    root_window.destroy()

def pophandler(e):
    file.tk_popup(e.x_root, e.y_root, 0)


txt1 = Text(win)
txt1.pack(fill=BOTH)

menubar = Menu(win)
win['menu']=menubar

file = Menu(menubar)
menubar.add_cascade(label='File', menu=file)

file.add_command(label='New', command=myhandler)
file.add_command(label='Open')
#file.add(itemType='command', label='Save') #thid works as does below
file.add_command(label='Save')
file.add_separator()
file.add_checkbutton(label='Save as', onvalue=1, offvalue=0)
#file.insert_command(3, label='Save Me')

rad1=Menu(file)
rad1.add_radiobutton(label='Option 1')
rad1.add_radiobutton(label='Option 2')
rad1.add_radiobutton(label='Option 3')

file.add_cascade(label='Options', menu=rad1)  #use add_cascade when adding a submenu
file.add_command(label="Exit", command=lambda: close_window(win))


settings=Menu(menubar)
menubar.add_cascade(label='Settings', menu=settings)
settings.add_command(label='Edit Settings')

txt1.bind('<Button-3>', pophandler)  #abdul on mac used Button-2 for right click.  Button-3 on windows

win.mainloop()