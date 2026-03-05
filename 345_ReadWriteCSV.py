
from tkinter import *
import csv
import tkinter.messagebox as msg

def onSelect(e):
    i = lstEmployee.curselection()[0]
    eid.set(data[i][0])
    ename.set(data[i][1])
    salary.set(data[i][2])

def onEntryChange():
    i = lstEmployee.curselection()[0]
    currValue = salary.get()
    if currValue != data[i][2]:
        ans = msg.showinfo(title='Value Change', message=f"Value Change to: {currValue}", default='ok', parent=win)
        data[i][2]=currValue
        

win = Tk()
win.title('Read and Write Employee Data From/To CSV')
win.geometry('600x400+100+10')   #+100+10 places the window
#win.resizable(True, True)  #x and y 


#################  Open the file and retrieve the data    ########################
with open('EmplSalaries.csv', 'r') as file:
    rdr = csv.reader(file)
    next(rdr)   #for this problem we can skip the header row
    data=[]
    nameList=[]
    for row in rdr:
        data.append(row)            #for populating the entry fields
        nameList.append(row[1])    #for populating the listbox



#################    Draw the window and incorporate the data   ################
#    ROW 0
#lblTitle
lblTitle = Label(win, text='Employee List')
lblTitle.grid(column=0,row=0)

lstVar = StringVar(value=nameList)

#List box
#create a vertical scroll bar
yScroll = Scrollbar(win, orient=VERTICAL, bg='blue',takefocus=True)
yScroll.grid(column=2, row=0)
lstEmployee = Listbox(win, height=1, listvariable=lstVar, selectmode=SINGLE, yscrollcommand=yScroll.set, )
lstEmployee.grid(column=1, row=0, columnspan=2)
#connect the listbox to the scrollbar
yScroll.config(command=lstEmployee.yview)


lstEmployee.bind("<<ListboxSelect>>", onSelect)

#numerous examples using PACk in a FRAME for window layout

##  ROW 1

#employee ID label
lblEmployeeID = Label(win, text='Employee ID')
lblEmployeeID.grid(column=0, row=1)

eid = StringVar()
txtEmployeeID = Entry(win, textvariable=eid)
txtEmployeeID.grid(column=1, row=1)

# Name Label
lblName  = Label(win, text='Name')
lblName.grid(column=2, row=1)

#name text box
ename=StringVar()
txtName = Entry(win, textvariable=ename )
txtName.grid(column=3, row=1)

#  ROW 2

lblSalary = Label(win, text='Salary')
lblSalary.grid(column=0, row=2)

salary = StringVar()
txtSalary = Entry(win, textvariable=salary)
txtSalary.grid(column=1, row=2)
#salary.trace_add("write", onEntryChange)


btnUpdate = Button(win, text='Update', command=onEntryChange)
btnUpdate.grid(column=1, row=3)

btnSaveX = Button(win, text='Save & Exit')
btnSaveX.grid(column=3, row=3)



win.mainloop()