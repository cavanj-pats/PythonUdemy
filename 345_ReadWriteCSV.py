
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
        ans = msg.askyesno(title='Value Change', message=f"Change Salary to: {currValue}", default='yes', parent=win)
        if ans == True:
            data[i][2]=currValue


def saveExit():
    write_csv = open('Employees.csv', 'w', newline='')
    wrtr = csv.writer(write_csv)
    wrtr.writerow(headings)
    wrtr.writerows(data)
    write_csv.close()
    win.quit()


win = Tk()
win.title('Read and Write Employee Data From/To CSV')
win.geometry('600x400+100+10')   #+100+10 places the window
#win.resizable(True, True)  #x and y 


#################  Open the file and retrieve the data    ########################
with open('EmplSalaries.csv', 'r') as file:
    rdr = csv.reader(file)
    headings = next(rdr)   #for this problem we can skip the header row
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

btnSaveX = Button(win, text='Save & Exit', command=saveExit)
btnSaveX.grid(column=3, row=3)



win.mainloop()




"""
                from tkinter import *
                from tkinter.font import *
                import csv


                def show_data(e):
                    i = enames.index(var1.get())
                    id_var.set(data[i][0])
                    name_var.set(data[i][1])
                    sal_var.set(data[i][2])


                def update():
                    i = enames.index(var1.get())
                    data[i][0] = id_var.get()
                    data[i][1] = name_var.get()
                    data[i][2] = sal_var.get()


                def save():
                    file_csv.close()
                    write_csv = open('Employees.csv', 'w', newline='')
                    wrtr = csv.writer(write_csv)
                    wrtr.writerow(headings)
                    wrtr.writerows(data)
                    write_csv.close()
                    win.quit()


                win = Tk()
                win.geometry('800x250')
                fnt = Font(family='Times new Roman', size=25)

                file_csv = open('Employees.csv', 'r')
                reader = csv.reader(file_csv)

                headings = next(reader)
                data = [row for row in reader]

                enames = [row[1] for row in data]

                var1 = StringVar(value=enames[0])
                opt1 = OptionMenu(win, var1, *enames, command=show_data)

                lst_label = Label(win, text='Employee List', font=fnt)
                id_label = Label(win, text='Employee ID', font=fnt)
                name_label = Label(win, text='Name', font=fnt)
                sal_label = Label(win, text='Salary', font=fnt)

                id_var = StringVar()
                name_var = StringVar()
                sal_var = StringVar()

                id_entry = Entry(win, textvariable=id_var, font=fnt)
                name_entry = Entry(win, textvariable=name_var, font=fnt)
                sal_entry = Entry(win, textvariable=sal_var, font=fnt)

                update_button = Button(win, text='Update', command=update, font=fnt)
                save_button = Button(win, text='Save & Exit', command=save, font=fnt)

                lst_label.grid(row=0, column=0)
                opt1.grid(row=0, column=1)
                id_label.grid(row=1, column=0)
                id_entry.grid(row=1, column=1)
                name_label.grid(row=1, column=2)
                name_entry.grid(row=1, column=3)
                sal_label.grid(row=2, column=0)
                sal_entry.grid(row=2, column=1)
                update_button.grid(row=3, column=0, columnspan=2)
                save_button.grid(row=3, column=2, columnspan=2)


                win.mainloop()

"""