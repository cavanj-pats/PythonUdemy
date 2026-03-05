#334_MenuWidget.py

## my code is a mixture of what I had orignally that worked but drew teh shape while dragging
## abdul's code pasted below and remarked has a draw function
##that is needed for drawing.
##while dragging only need to report out on the coordinates
##rely's on global 'drawing' variable and on x2, y2 IntVar tied to canvas apparently.

from tkinter import *  # type: ignore
#from tkinter.font import *

#from tkmacosx import *

drawing = None

def close_window(root_window):
    root_window.destroy()

def pophandler(e):
    mshape.tk_popup(e.x_root, e.y_root, 0)

def draw_begin(e):
    # need to get the shape, color, weight
    # e shoudl provide the x0, y0
    global isDrawing, startx, starty
    isDrawing = True
    startx = e.x
    starty = e.y
    x2.set(e.x)
    y2.set(e.y)
    draw()

def dragging(e):
    if isDrawing == True:
        can1.coords(drawing, startx, starty, e.x, e.y)

def draw():
    global drawing, isDrawing, startx, starty
    if isDrawing == True:
        drwShape = shapeVar.get()
        if drwShape == 'line':
            drawing = can1.create_line(startx, starty, x2.get(), y2.get(), fill=cVar.get(), width=wtVar.get())
        elif drwShape == 'rectangle':
            drawing = can1.create_rectangle(startx, starty, x2.get(), y2.get(), outline=cVar.get(), width=wtVar.get())
        elif drwShape == 'circle' :
            drawing= can1.create_oval(startx, starty, x2.get(), y2.get(), outline=cVar.get(), width=wtVar.get())


def draw_stop(e):
    global isDrawing, startx, starty
    isDrawing = False
    startx = None
    starty = None



win = Tk()
win.title('Drawing  Application!')
win.geometry('600x400')   #add +100+10 places the windowget()

global isDrawing
isDrawing = False

global startx, starty
x2 = IntVar()
y2 = IntVar()

menubar = Menu(win)
win['menu']=menubar

############.     Shape Menu
mshape = Menu(menubar)
menubar.add_cascade(label='Shape', menu=mshape)

shapeVar = StringVar(value='line')
mshape.add_radiobutton(label='Line', variable=shapeVar, value= 'line')
mshape.add_radiobutton(label='Rectangle', variable=shapeVar, value='rectangle')
mshape.add_radiobutton(label='Circle', variable=shapeVar, value='circle')
mshape.add_separator()
mshape.add_command(label="Exit", command=lambda: close_window(win))
#################### end shape menu

cVar = StringVar(value='red')
color=Menu(menubar)
menubar.add_cascade(label='Color', menu=color)
color.add_radiobutton(label='Red', variable=cVar, value='red')
color.add_radiobutton(label='Green', variable=cVar, value='green')
color.add_radiobutton(label='Blue', variable=cVar, value='blue')
########################## end Color Menu


wtVar = IntVar(value=1)
weight=Menu(menubar)
menubar.add_cascade(label='Weight', menu=weight)
weight.add_radiobutton(label='1.0', variable=wtVar, value =1)
weight.add_radiobutton(label='2.0' , variable=wtVar, value=2)
weight.add_radiobutton(label='3.0' , variable=wtVar, value=3)
########################### end Weight Menu


#txt1.bind('<Button-3>', pophandler) #abdul on mac used Button-2 for right click.  Button-3 on windows

can1 = Canvas(win, bg='yellow', width=600, height=400)
can1.pack()

# i think left click down record x0 y0. left click up record x1, y1
#then look at menu selection and draw the shape accordingly

can1.bind("<Button-1>", draw_begin)

can1.bind("<B1-Motion>", dragging)

can1.bind("<ButtonRelease-1>", draw_stop)


win.mainloop()


##.   Abdul code.  I incorported drawing variable and 
##  and created dragging function.  I was getting multiple shapes
##.  i changed draw to be just a funciton and incporated dragging as the bound event handler
"""
                    from tkinter import *


                    drawing = None

                    def first_point(e):
                        pressflag.set(True)
                        x1.set(e.x)
                        y1.set(e.y)
                        x2.set(e.x)
                        y2.set(e.y)
                        draw_shape()


                    def dragging(e):
                        if pressflag.get() == True:
                            can1.coords(drawing, x1.get(), y1.get(), e.x, e.y)


                    def second_point(e):
                        can1.coords(drawing, x1.get(), y1.get(), e.x, e.y)
                        pressflag.set(False)


                    def draw_shape():
                        global drawing
                        funs = [can1.create_line, can1.create_rectangle, can1.create_oval]
                        if shape_var.get() == 0:
                            drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(), fill=color_var.get(), width=width_var.get())
                        else:
                            drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(), outline=color_var.get(), width=width_var.get())


                    win = Tk()
                    win.geometry('600x400')

                    can1 = Canvas(win, bg='#ffffbb')
                    can1.pack(fill=BOTH, expand=True)

                    can1.bind('<ButtonPress>', first_point)
                    can1.bind('<ButtonRelease>', second_point)
                    can1.bind('<Motion>', dragging)

                    shape_var = IntVar(value=0)
                    color_var = StringVar(value='red')
                    width_var = IntVar(value=3)

                    x1 = IntVar(value=0)
                    y1 = IntVar(value=0)
                    x2 = IntVar(value=0)
                    y2 = IntVar(value=0)
                    pressflag = BooleanVar(value=False)

                    menubar = Menu(win)

                    shape_menu = Menu(menubar)
                    shape_menu.add_radiobutton(label='Line', variable=shape_var, value=0)
                    shape_menu.add_radiobutton(label='Rectangle', variable=shape_var, value=1)
                    shape_menu.add_radiobutton(label='Oval', variable=shape_var, value=2)
                    menubar.add_cascade(label='Shapes', menu=shape_menu)

                    color_menu = Menu(menubar)
                    color_menu.add_radiobutton(label='Red', variable=color_var, value='red')
                    color_menu.add_radiobutton(label='Green', variable=color_var, value='green')
                    color_menu.add_radiobutton(label='Blue', variable=color_var, value='blue')
                    menubar.add_cascade(label='Colors', menu=color_menu)

                    width_menu = Menu(menubar)
                    width_menu.add_radiobutton(label='1', variable=width_var, value=1)
                    width_menu.add_radiobutton(label='3', variable=width_var, value=3)
                    width_menu.add_radiobutton(label='5', variable=width_var, value=5)
                    menubar.add_cascade(label='Thickness', menu=width_menu)


                    win['menu'] = menubar

                    win.mainloop()
"""