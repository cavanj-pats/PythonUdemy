#window_TK_numeric.py
#styles and options used for Scale, scrollbar, and Spinbox controls



from tkinter import *
#from tkmacosx import *


win = Tk()
win.title('First Application!')
win.geometry('600x400+100+10')   #+100+10 places the window
win.resizable(True, True)  #x and y 


sb1 = Scrollbar(win, orient=VERTICAL)
t1 = Text(win)

t1.config(yscrollcommand=sb1.set)
sb1.config(command=t1.yview)

sb1.pack(side=RIGHT, fill=Y)  #scroll bar to the right of the text
t1.pack(side=LEFT, fill=Y)  #text is to the left of the scrollbar



"""
    var   Scale only
    StringVar for string
    from_ and to  - both Scale and Spinbox


    orient (HORIZONTAL or VERTICAL)
"""


var = IntVar(value=20)  #initial value of the Scale.
s1=Scale(win,variable=var, from_=0, to=100, orient=HORIZONTAL)
s1.pack()

sp1=Spinbox(win, from_=0, to=100, format='%2.2f')
sp1.pack()



win.mainloop()