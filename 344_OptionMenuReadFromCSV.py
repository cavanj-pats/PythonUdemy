#342_OptionMenu.py

from tkinter import *  # type: ignore
import csv

def optSelection(value):
    i = header.index(optVar.get())
    col = [d[i] for d in data]
    lst1.delete(0, END)
    lst1['listvariable'] = Variable(value=col)


win = Tk()
win.title('Option Menu Challenge')
win.geometry('400x300')   #add +100+10 places the windowget()

##                             Read the employee data from a file
f = open('EmplSalaries.csv', 'r')
#rdr = csv.DictReader(f)
rdr = csv.reader(f)

header = next(rdr)
data = []

for row in rdr:
    data.append(row)

f.close()





optVar = StringVar(value=header[0])

#from tkdocs  OptionMenu(parent, variable, choice1, choice2,....)  #used *choice to show the collection
optMnu1 = OptionMenu(win, optVar,  *header, command=optSelection ) 
optMnu1.pack()

#apparently abdul hard coded the employee ID's as a variable
#knowing that was the first key
eids = [d[0] for d in data]
#build the list box
listData = Variable(value=eids)
#the default selection will be [*opDict][0] so teh default listbox contents should be based on that

lst1 = Listbox(win, listvariable=listData)
lst1.pack()




win.mainloop()


"""
        ABDUL CODE FROM GITHUB

                            from tkinter import *


                    def change(e):
                        lstvar = Variable(value=dict1[var1.get()])
                        lst1.delete(0, END)
                        lst1['listvariable'] = lstvar


                    win = Tk()
                    win.geometry('400x300')

                    dict1 = {'Languages': ['C', 'C++', 'Java'],
                            'Databases': ['Oracle', 'SQL Server', 'mysql', 'Mango DB'],
                            'Clouds': ['AWS', 'SalesForce', 'MS Asure']}

                    var1 = StringVar(value='Languages')

                    opt1 = OptionMenu(win,  var1, *dict1.keys(), command=change)
                    opt1['fg'] = 'blue'

                    opt1.pack()

                    lstvar1 = Variable(value=dict1['Languages'])

                    lst1 = Listbox(win, listvariable=lstvar1)
                    lst1.pack()

                    win.mainloop()

"""