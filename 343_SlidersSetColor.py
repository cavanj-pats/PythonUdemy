#343_SlidersSetColor.py

from tkinter import *  # type: ignore

#remember scales require a lambda function. see below. 
#the function won't be invoked

def onChange():
    r = red.get()
    g= green.get()
    b= blue.get()
    color = f"#{r:02x}{g:02x}{b:02x}"   #convert decimal to hex
    lbl1['bg']=color
    lbl1.config(fg=color)




win = Tk()
win.title('Option Menu Challenge')
win.geometry('400x300')   #add +100+10 places the windowget()

lbl1 = Label(win, bg='white', fg='white', text='Some Hidden Text')
lbl1.pack()

rdVar = IntVar(value=0)
red = Scale(win, from_=0, orient=HORIZONTAL, to=255, label='R',variable=rdVar, command=lambda x : onChange() )
red.pack()

grnVar = IntVar(value=0)
green = Scale(win, from_=0, to=255, orient=HORIZONTAL,label='G' , variable=grnVar, command=lambda x : onChange())
green.pack()

blVar = IntVar(value=0)
blue = Scale(win, from_=0, to=255, orient=HORIZONTAL, label='B',variable=blVar, command=lambda x : onChange())
blue.pack()


win.mainloop()

##### INSTRUCTOR CODE
"""
        from tkinter import *


        def change_color(e):
            r = red_var.get()
            g = green_var.get()
            b = blue_var.get()
            color_lbl['bg'] = f'#{r:02x}{g:02x}{b:02x}'


        win = Tk()
        win.geometry('300x200')

        color_lbl = Label(win, text='', bg='black', width=30)
        color_lbl.grid(row=0, column=0, columnspan=2)

        red_lbl = Label(win, text='Red')
        green_lbl = Label(win, text='Green')
        blue_lbl = Label(win, text='Blue')

        red_lbl.grid(row=1, column=0)
        green_lbl.grid(row=2, column=0)
        blue_lbl.grid(row=3, column=0)

        red_var = IntVar(value=0)
        green_var = IntVar(value=0)
        blue_var = IntVar(value=0)

        red_scale = Scale(win, orient=HORIZONTAL, variable=red_var, from_=0, to=255, command=change_color)
        green_scale = Scale(win, orient=HORIZONTAL, variable=green_var, from_=0, to=255, command=change_color)
        blue_scale = Scale(win, orient=HORIZONTAL, variable=blue_var, from_=0, to=255, command=change_color)

        red_scale.grid(row=1, column=1)
        green_scale.grid(row=2, column=1)
        blue_scale.grid(row=3, column=1)

        win.mainloop()

"""