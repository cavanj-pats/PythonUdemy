#339_FontOptions


from tkinter import *  # type: ignore
from tkinter.font import Font

#from tkinter.font import *

#from tkmacosx import *

"""
    I copied abdul's code after struggling
    i think mine would have worked with teh if else blocks
    had i restated the font family and size
    i did not do that and my text size shrank
    his fnt line re-establishes the entire font configuration
    whereas i was using .configure to adjust only the elements i wnated to change
    the guidance on font seemed to indicate tis was a way to 
    change just one option.
"""

def format():
    #check the value and apply bold, italic, underline format
    
    b = ['bold' if vBold.get() == 1 else 'normal'][0]
    i = ['italic' if vItalic.get() == 1 else 'roman'][0]
    fnt = Font(family='Times new Roman', size=45, weight=b, slant=i, underline=vUline.get())
    lbl1['font'] = fnt



win = Tk()
win.title('Stop watch challenge Application!')
win.geometry('400x200')   #add +100+10 places the windowget()




#ff5555 would have red and some green and some blue.   RGB
lbl1 = Label(win, bg='red', fg='yellow', text='Hello World' )
lbl1['font']=(Font(family = 'Times New Roman' , size = 45))
#lbl1.pack(fill=BOTH, expand=True)  #not 'both' and not 1 vs BOTH and True
lbl1.grid(column=0,columnspan=3,row=0)  #grid column, columnspan row
#could not use textvariable with a var =StrValue()
#could not assign value to var in function.
vBold = IntVar(value = 0)
chkBold = Checkbutton(win, text='Bold',variable=vBold, onvalue=1, offvalue=0 ,command=format)
chkBold.grid(column=0,columnspan=1,row=1)

vItalic = IntVar(value = 0)
chkItalic = Checkbutton(win, text='Italic', variable=vItalic, onvalue=1, offvalue=0 ,command=format)
chkItalic.grid(column=1,columnspan=1,row=1)

vUline = IntVar(value = 0)
chkUline = Checkbutton(win, variable=vUline, offvalue=0, onvalue=1, text='Underline', command=format)
chkUline.grid(column = 2,columnspan=1,row=1)






win.mainloop()