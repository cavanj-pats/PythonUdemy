#339_FontOptions


from tkinter import *  # type: ignore
import random


#from tkinter.font import *

#from tkmacosx import *

def shuffle_list():
    all_items = lst1.get(0, END)
    all_items_list = list(all_items)
    random.shuffle(all_items_list)
    lst1.delete(0, END)

    for item in all_items_list:
        lst1.insert(END, item)

def on_double_click(e):
    selItem = lst1.curselection()
    strText.set(lst1.get(selItem))


win = Tk()
win.title('List Box - Shuffle and Select')
win.geometry('400x300')   #add +100+10 places the windowget()

strText = StringVar(value= 'Selected Item')

#ff5555 would have red and some green and some blue.   RGB
lbl1 = Label(win, bg='black', font=('Times New Roman', 25), fg='yellow', textvariable=strText )
#lbl1['font']=(Font(family = 'Times New Roman' , size = 45))
#lbl1.pack(fill=BOTH, expand=True)  #not 'both' and not 1 vs BOTH and True
lbl1.pack()


list_items = ['Python', 'Java', 'C++', 'Ruby', 'Javascript', 'C Lang', 'C#', 'Go', 'Swift']
listVar = StringVar(value=tuple(list_items))

lst1 = Listbox(win, selectmode=EXTENDED, listvariable=listVar)

"""
lst1.insert(0, 'Python')
lst1.insert(1, 'Java')
lst1.insert(2, 'C++')
lst1.insert(3, 'JavaScript')
lst1.insert(4, 'Ruby')
lst1.insert(5, 'C Lang')
lst1.insert(6, 'PHP')
lst1.insert(7, 'C#')
lst1.insert(8, 'R')
lst1.insert(9, 'Swift')
lst1.insert(10, 'Android')
lst1.insert(11, 'VB')
lst1.insert(12, 'PERL')
lst1.insert(13, 'Kotlin')
lst1.insert(14, 'Go')
lst1.insert(15, 'Scala')
"""

lst1.pack()

btn1 = Button(win, text='Shuffle', command=shuffle_list)
lst1.bind("<Double-1>", on_double_click)
#lst1.bind("<<ListboxSelect>>", on_double_click)


btn1.pack()


win.mainloop()