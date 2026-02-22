#window_TK_styles.py

# Various style options and settings for use in Entry, Text, Label, and List Boxes
#  graphics  bitmap or image

from tkinter import * # type: ignore
#from tkmacosx import *


win = Tk()
win.title('First Application!')
win.geometry('600x400+100+10')   #+100+10 places the window
win.resizable(True, True)  #x and y 

#button style options
#  border or bd for cm  1i ing  1m milimeter
#  color  RGB  Red green blue.  0 - 255.  or in Hex  00-ff   '#ff0000'
# anchor is where you want the text in teh button. NE, N, NE, E, SE, S, SW, W, CENTER.  Constants
# relief:  flat, sunken, raised
#overrelief Sunken, Groove, Ridge
b1 = Button(win, text='Button 1', bd=10, bg='red', fg='yellow')  #  10, 1, 1c 
#not yet discussed pack options which I believe there are a few
b1.pack()

#Widget Opions   Text / Item Selection and Text insertion Cursor
"""
    selectbackground 
    selectforeground
    selectborderwidth

"""

"""
    insertofftime
    insertontime   
    cursor='pencil', 'plus', 'crackpipe    #for drawing 
"""

e1 = Entry(win, insertontime=10, insertofftime=8, insertwidth=5, insertbackground='blue', selectbackground='yellow', selectforeground='blue', selectborderwidth=10)
e1.pack()




# Text is multiline text
"""
    wrap (CHAR, WORD, NONE) - Default is character wise wrapping. Can be word, or none 
    wraplength - label widget
    spacing1 - where first row starts
    spacing2  - spacing between rows
    spacing3  - gap at bottom after last row.  Need scrollbar to show us
"""
e2 = Text(win,height='2', width='20', insertbackground='red', insertwidth=5, insertborderwidth=5, selectbackground='yellow', selectforeground='blue', selectborderwidth=10)
e2.pack()

###
#   bitmap='warning' changes text to exclamation point
###

img = PhotoImage(file='icons8-python-48.png')
l1 = Label(win, text='abcdefghijklmnopqrstuvwxyz', width=100, wraplength=100, image=img)
l1.pack()

####      exportselection most useful in listbox  keep or lose selection when moving to another control
#####  By default, the user may select text with the mouse, and the selected text will be exported 
# ###  to the clipboard. To disable this behavior, use exportselection=0.

lb1 = Listbox(win, selectbackground='yellow', selectforeground='blue', selectborderwidth=10, exportselection=False)
lb1.insert(0, 'AAAA')
lb1.insert(1, 'BBBB')
lb1.insert(2, 'CCCC')
lb1.insert(3, 'DDDD')
lb1.pack()


win.mainloop()
