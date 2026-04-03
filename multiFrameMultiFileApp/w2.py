#w2.py
#i dont know if this will be one W2 or if it will be all applicable w2's

#need to add functionality for mnore than one W2 to be created.

import tkinter as tk

SMALL_FONT = ("Arial", 8)

class W2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="W2")
        self.label.pack()
        
        self.box1 = tk.Label(self, text="1 Wages", font=SMALL_FONT)
        self.box1.pack()
        varBox1 = tk.StringVar() #will need to convert to float
        self.entry1 = tk.Entry(self, textvariable=varBox1)
        self.entry1.pack()
        self.box2 = tk.Label(self, text='Fed Income Tax Witheld', font=SMALL_FONT )
        self.box2.pack()
        varBox2 = tk.StringVar()
        self.entry2 = tk.Entry(self, textvariable=varBox2)
        self.entry2.pack()

        varBox3 = tk.StringVar()
        self.lblBox3 = tk.Label(self, text='Soc Sec Wages', font=SMALL_FONT)
        self.lblBox3.pack()
        self.Box3 = tk.Entry(self, textvariable=varBox3 )
        self.Box3.pack()
        
        btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame("FrameB") ) 
        btn.pack()
        #all other controls and functionality go here
        """
            box 1 wages
            box 2 fed income tax witheld
            3 soc sec wages
            4 soc sec tax witheld
            6 medicare tax witheld
            d control number
            c employer
            b employer fed id number
            a employee soc sec number
            12a.  code and value
            12b.   code and value
            12c
            12d
            13 stat emp. ret plan.  3rd party sick pay. checkboxes
            15.  state
            16 state wages tips
            17 state income tax

            figure out a stack of the previous frame or window

        """