#342_OptionMenu.py

from tkinter import *  # type: ignore

def optSelection(value):
    #change the list box data based on selection of optionmenu
    listData.set(optDict[value])



win = Tk()
win.title('Option Menu Challenge')
win.geometry('400x300')   #add +100+10 places the windowget()

#the options presented to the user
optText = ["Languages", "Databases", "Clouds"]   #this variable is used below to set default listbox contents

#the data associated with the selected option
data = [ ['C++', 'Python', 'C Lang'] ,   ['Oracle', 'SQLite', 'MongoDB'], ['Azure', 'iCloud', 'DropBox'] ]

optDict = dict(zip(optText, data))   #[*optDict] #uses list comprehensions to return a list of keys unpack operator

optVar = StringVar()
optVar.set([*optDict][0])

#from tkdocs  OptionMenu(parent, variable, choice1, choice2,....)  #used *choice to show the collection
optMnu1 = OptionMenu(win, optVar,  *optDict, command=optSelection ) 
optMnu1.pack()


#build the list box
listData = StringVar()
#the default selection will be [*opDict][0] so teh default listbox contents should be based on that
listData.set(optDict[optText[0]])    #default lisbox contents based on default selection of optionmenu
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