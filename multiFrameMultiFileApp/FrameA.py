# FrameA.py
import tkinter as tk
#from FrameB import FrameB

SMALL_FONT = ("Arial", 7)

class FrameA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Frame A")
        self.label.grid(column=0, row=0, columnspan=3, sticky=tk.W)

        srow = 2 #start row of the data grid

        
        #First Name and Middle Initial.  takes up two rows
        self.var_fname = tk.StringVar()
        self.lbl_fname = tk.Label(self, text='Your first name and middle initial', font=SMALL_FONT)
        self.lbl_fname.grid(column=0, row=srow, sticky=tk.W)
        self.fname = tk.Entry(self, textvariable=self.var_fname)   
        self.fname.grid(column=0, row=srow+1, columnspan=2, stick=tk.W+tk.E)

        self.var_lname = tk.StringVar()
        self.lbl_lname = tk.Label(self, text='your last name',
                                  font=SMALL_FONT)
        self.lbl_lname.grid(column=2, row= srow, columnspan=2, sticky=tk.W)
        self.lname = tk.Entry(self, textvariable=self.var_lname)
        self.lname.grid(column=2, row=srow+1, columnspan=3, sticky=tk.W+tk.E)

        self.var_socsec = tk.StringVar()
        self.lbl_socsec = tk.Label(self, text='Your social security number', 
                                   font=SMALL_FONT)
        self.lbl_socsec.grid(column=5, row=srow, columnspan=2)
        self.socsec = tk.Entry(self, textvariable=self.var_socsec, width=12)
        self.socsec.grid(column=5, row=srow+1, columnspan=2,sticky=tk.W+tk.E)


        #Spouse First name and middle initial
        self.var_sfname = tk.StringVar()
        self.lbl_sfname = tk.Label(self, text='If joint return, spouses first name and middle initial', 
                                   font=SMALL_FONT)
        self.lbl_sfname.grid(column=0, row=srow+2, sticky=tk.W) 
        self.sfname = tk.Entry(self, textvariable=self.var_sfname)
        self.sfname.grid(column=0, row= srow+3, columnspan=2, sticky=tk.W+tk.E)     

        self.var_slname = tk.StringVar()
        self.lbl_slname = tk.Label(self, text='spouse last name',
                                  font=SMALL_FONT)
        self.lbl_slname.grid(column=2, row=srow+2, columnspan=2, sticky=tk.W)
        self.slname = tk.Entry(self, textvariable=self.var_slname)
        self.slname.grid(column=2, row=srow+3, columnspan=3, sticky=tk.W+tk.E)

        self.var_ssocsec = tk.StringVar()
        self.lbl_ssocsec = tk.Label(self, text='Your social security number', 
                                   font=SMALL_FONT)
        self.lbl_ssocsec.grid(column=5, row=srow+2, columnspan=2)
        self.ssocsec = tk.Entry(self, textvariable=self.var_ssocsec, width=12)
        self.ssocsec.grid(column=5, row=srow+3, columnspan=2, sticky=tk.W+tk.E)

        self.lblFilingStatus = tk.Label(self, text='Filing Status')
        self.lblFilingStatus.grid(column=0, row=srow+4, sticky=tk.W)
        



        self.btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame("FrameB") )  #Example logic
        self.btn.grid(column=5, row=srow+15, columnspan=2)

        label_line11_income=tk.Label(self)
        label_line11_income.grid(column=4, row=0, columnspan=3)  #put result of calculation here