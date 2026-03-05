#346_FrameAndLabelFrame.py


from tkinter import * # pyright: ignore[reportWildcardImportFromLibrary]
from PIL import Image, ImageTk



win = Tk()
win.geometry('600x400')
win.title('348 Canvas')

can1 = Canvas(win, bg='yellow', width=600, height=400)
can1.pack()

can1.create_line(100,100,200,200, fill='red', arrow=LAST, width=5)
can1.create_rectangle(100,100,200,200, outline='black', width= 2)
can1.create_oval(200,200,350,300, width=2, outline='blue' )
can1.create_arc(40,30,150,150, width=3, outline='green', start=90, extent=180 )
can1.create_text(80,10, text='Drawing Canvas', fill='blue', anchor=NW)

img1 = ImageTk.PhotoImage(Image.open("python1.webp"))
can1.create_image(440,150, image=img1)

btn1 = Button(win, text='Click Me!')

can1.create_window(380,300, window=btn1)

win.mainloop()

