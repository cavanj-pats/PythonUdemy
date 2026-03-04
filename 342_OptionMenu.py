#342_OptionMenu.py

from tkinter import *  # type: ignore


win = Tk()
win.title('Option Menu Challenge')
win.geometry('400x300')   #add +100+10 places the windowget()

optText = ["Languages", "Databases", "Clouds"]

drill = dict({ [ ["Languages"] , ['C++', 'Python', 'C Lang'] ],
         [ ["Databases"] , ['Oracle', 'SQLite', 'MongoDB']],
          ["Clouds"] , ['Azure', 'iCloud', 'DropBox'] })

optMnu1 = OptionMenu(win, variable=optText,  *drill ) 
optMnu1.pack()





win.mainloop()