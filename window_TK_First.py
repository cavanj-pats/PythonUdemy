

from tkinter import *
#from tkmacosx import *


win = Tk()
win.title('First Application!')
win.geometry('600x400+100+10')   #+100+10 places the window
win.resizable(True, True)  #x and y 
#win.attributes('-alpha',0.55)   #-alpha, 0.25 made window transparent, can keep messing with the float value.  opaqueness level

#add a label
l = Label(win, text='Hello World')  # create a label reference the window it will be in
l.pack()  #add label to the window

#text box
var='OK'
e = Entry(win, textvariable='var')
e['justify']='right'  #entry does not have anchor

e.pack()

#button
#properties can be added when you set up the object, or in dictionary form or using config function
#properties are also known as options.  for config can also use configure (the entire word)
cmdOK = Button(win, text= var, width=4, height=2)
cmdOK['bd']=2  #'border depth'
cmdOK['anchor']='sw'    #ne northeast,  nw, sw  anchors text in a corner.  
cmdOK['font']='Ariel, 20'  #abdul also used cmdOK.config(font='Ariel, 20)
cmdOK['fg']='yellow'
cmdOK['padx']=2
cmdOK['pady']=2
cmdOK.pack()

#text area in Tkinter - text
t = Text(win, width=30, height=10)
t.pack()

c = Checkbutton(win, text='Yes')
c.pack()

r= Radiobutton(win, text='Option 1', variable='v1', value=1)
r.pack()
r2 = Radiobutton(win, text='Option 2', variable='v1', value=2)
r3 = Radiobutton(win, text='Option 3', variable='v1', value=3)
r2.pack()
r3.pack()

#option menu or listbox/combobox
v = StringVar()
opt=OptionMenu(win, v, 'Python', *('Java','C++', 'Javascript','Python'))
opt.pack()

#scale or slider or sliding bar
s = Scale(win, from_=0, to=100)
s.pack()




win.mainloop()


