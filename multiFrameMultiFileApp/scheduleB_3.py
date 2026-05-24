#this will be Schedule B Form 1040

import tkinter as tk
#from FrameB import FrameB

SMALL_FONT = ("Arial", 7)

"""   ***this is the interface ***
Part I
Line 1 data:  self.entries
Line 2 (calculated entry):  self.line2Text
Line 3 (manual entry_): self.line3Text
Line 4 (calculated):  self.line4Text

Part II
Line 5 data: self.part2_entries
Line 6 (calculated):  self.line6Text

Part III
Line 7a checkbox: self.var7a_1
Line 7b checkbox: self.var7a_2
Text Field: selfvarLine7b
Line 8: self.varLine8


"""

class ScheduleB_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entries = {}


        self.leftFrame = tk.Frame(self, padx=0, pady=0)
        self.leftFrame.grid(column=0, row=0, rowspan=2, sticky=tk.N)

        

        #use this frame for header labels
        self.headerFrame = tk.Frame(self, padx=0, pady=0)
        self.headerFrame.grid(column=1, row=0, sticky=tk.W+tk.N)
        
        

        #data table frame
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(column=1, row=1, sticky=tk.W+tk.N)
        
        

        ##   ***************    End Part II   Start Part III ***********************************************************
        
        self.lblPart3 = tk.Label(self.leftFrame, text="Part III Foreign Accounts and Trusts", padx=0,pady=15)
        self.lblPart3.grid(column=0,row=4)

        self.lblPart3note=tk.Label(self.leftFrame, font=SMALL_FONT, text="**CAUTION**: If required, failure to file FinCEN " \
                                   "Form 114 may result in substantial penalties. " \
                                    "Additionally, you may be required to file Form 8938, Statement of Specified " \
                                        "Foreign Financial Assets. See instructions" , wraplength=85 )
        self.lblPart3note.grid(column=0, row=5)

        
        
        
      

        self.lblPart3_header = tk.Label(self.dataFrame, text= "Part III - You must complete this part if you (a) had over $1,500 "\
                                        "of taxable interest or ordinary dividends; (b) had a foreign "\
                                        "account; or (c) received a distribution from, or were a grantor "\
                                            "of, or a transferor to, a foreign trust.", wraplength=500, font='Arial 6')
        self.lblPart3_header.grid(column=0, columnspan=2, row=0, pady=4, sticky=tk.NW)

        self.lblLine7a = tk.Label(self.dataFrame, font=SMALL_FONT, text=" 7a. At any time during 2025, did you have a financial "\
                                  "interest in or signature authority over a financial "\
                                    "account (such as a bank account, securities account, or brokerage account) "\
                                     "located in a foreign country? See instructions", wraplength=400, justify="left")
        self.lblLine7a.grid(column=0, row=1, sticky=tk.NW)
        self.varLine7a_1 = tk.IntVar()
        self.cb7a_1 = tk.Checkbutton(self.dataFrame, variable= self.varLine7a_1)
        self.cb7a_1.grid(column=1, row=2)

        self.lblLine7a_2 = tk.Label(self.dataFrame, font=SMALL_FONT, text=" ... If Yes, are you required to file FinCEN Form 114, "\
                                    "Report of Foreign Bank and Financial Accounts (FBAR), to report that financial interest "\
                                    "or signature authority?  See applicable instructions", 
                                     wraplength=400, justify="left")
        self.lblLine7a_2.grid(column=0, row=3, sticky=tk.NW)
        self.varLine7a_2 = tk.IntVar()
        self.cbLine7a_2 = tk.Checkbutton(self.dataFrame, variable= self.varLine7a_2)
        self.cbLine7a_2.grid(column=1, row=3)
        self.lblLine7b = tk.Label(self.dataFrame, font=SMALL_FONT, text="If you are required to file FinCEN Form 114, list the name(s) "\
                                  "of the foreign country(-ies) where the financial account(s) is (are) located:", 
                                  wraplength=400)
        self.lblLine7b.grid(column=0, row=4)
        self.varLine7b = tk.StringVar()
        self.dataLine7b = tk.Entry(self.dataFrame, textvariable=self.varLine7b, width=75)
        self.dataLine7b.grid(column=0, row=5, columnspan=2, sticky=tk.NW)

        self.lblLine8 = tk.Label(self.dataFrame, font=SMALL_FONT, text="During 2025, did you receive a distribution from, or were you "\
                                 "the grantor of, or transferor to, a foreign trust? If Yes, you may have to file Form 3520. "\
                                    "See instructions .", wraplength=400, justify="left")
        self.lblLine8.grid(column=0, row=6, sticky=tk.NW)
        self.varLine8 = tk.IntVar()
        self.cbLine8 = tk.Checkbutton(self.dataFrame, variable= self.varLine8)
        self.cbLine8.grid(column=1, row=6)

        

        ##################################    End Part III **********************************************###
        #for navigation from here go back to the 1040 form

        self.btnFrameA =tk.Button(self.leftFrame, text="Frame A", 
                         command=lambda: controller.show_frame("FrameA"))
        self.btnFrameA.grid(column=0, row=7)
        
    # function to sum Part I table and overall sum
    def update_sum(self, event):
        total = 0
        #self.entries is the entire grid.  Return one row at a time
        for rowEntry in self.entries:
            for entry in rowEntry:
                try:
                    # Get text from each entry and convert to float
                    val = float(entry.get())
                    total += val
                except ValueError:
                    # Ignore empty or non-numeric inputs
                    pass

  




