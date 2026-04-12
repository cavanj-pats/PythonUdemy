# FrameA.py
import tkinter as tk
#from FrameB import FrameB

SMALL_FONT = ("Arial", 8)

class FrameA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Frame A")
        self.label.grid(column=0, row=0, columnspan=6, sticky=tk.W)

        srow = 2 #start row of the data grid

        #First Name and Middle Initial.  takes up two rows
        self.var_fname = tk.StringVar()
        self.lbl_fname = tk.Label(self, text='Your first name and middle initial', font=SMALL_FONT)
        self.lbl_fname.grid(column=0, row=srow, sticky=tk.W)
        self.fname = tk.Entry(self, textvariable=self.var_fname)   
        self.fname.grid(column=0, row= srow+1, columnspan=2)



        #Souse First name and middle initial
        self.var_sfname = tk.StringVar()
        self.lbl_sfname = tk.Label(self, text='Your first name and middle initial', font=SMALL_FONT)
        self.lbl_sfname.grid(column=0, row=srow+2, sticky=tk.W) 
        self.sfname = tk.Entry(self, textvariable=self.var_sfname)
        self.sfname.grid(column=0, row= srow+3, columnspan=2)     


        self.btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame("FrameB") )  #Example logic
        self.btn.pack()
        label_line11_income=tk.Label(self)
        label_line11_income.pack()  #put result of calculation here