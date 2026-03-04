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
            import csv


            def show_data(e):
                i = headings.index(var1.get())
                col = [row[i] for row in data]
                lst1.delete(0, END)
                lst1['listvariable'] = Variable(value=col)


            win = Tk()
            win.geometry('400x300')

            file_csv = open('Employees.csv', 'r')
            reader = csv.reader(file_csv)

            headings = next(reader)
            data = []
            for t in reader:
                data.append(t)

            var1 = StringVar(value=headings[0])
            opt1 = OptionMenu(win, var1, *headings, command=show_data)
            opt1.pack()

            eids = [row[0] for row in data]

            lstvar1 = Variable(value=eids)
            lst1 = Listbox(win, listvariable=lstvar1)
            lst1.pack()

            win.mainloop()   

"""