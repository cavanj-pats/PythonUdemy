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

class ScheduleB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.leftFrame = tk.Frame(self, padx=0, pady=0)
        self.leftFrame.grid(column=0, row=0, rowspan=2, sticky=tk.N)

        self.lblPart1 = tk.Label(self.leftFrame, text='Part I interest', padx=0,pady=0)
        self.lblPart1.grid(column=0,row=0, sticky=tk.N)
        self.lblP1note = tk.Label(self.leftFrame, font=SMALL_FONT, text="(See instructions and the Instructions for Form 1040, "\
                                   " line 2b.) Note: If you received a Form 1099-INT, Form 1099-OID, or substitute statement from a brokerage firm, "\
                                    "list the firm’s name as the payer and enter the total interest "\
                                        "shown on that form. ------------------------------------------------" \
                                            "------------------------", wraplength=85)
        self.lblP1note.grid(column=0, row=1)

        
        

        #use this frame for header labels
        self.headerFrame = tk.Frame(self, padx=0, pady=0)
        self.headerFrame.grid(column=1, row=0, sticky=tk.W+tk.N)
        
        self.headerLabel = tk.Label(self.headerFrame, text= "1.  List name of payer. If any interest is " \
                                    "from a seller-financed mortgage and the " \
                                    "buyer used the property as a personal residence, " \
                                    "see the instructions and list this interest first. Also, show that "\
                                    "buyer’s social security number and address:",  wraplength=400, 
                                    font=SMALL_FONT, justify='left', padx=5, pady=0)
        
        self.headerLabel.pack()

        #data table frame
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(column=1, row=1, sticky=tk.W+tk.N)
        
        
        # i think i need to define the variable here, before i call i function that sets it
        self.line2Text = tk.StringVar(value="0")
        
        ####   Loop to build the table for Part I.  Also populates the self.entries list.
        rows, cols = 10, 2
        self.entries = []
        
        for r in range(rows):
            row_entries = []
            for c in range(cols):
                if c == 0:
                    w=60
                else:
                    w=15

                e = tk.Entry(self.dataFrame, width=w, font='Arial, 7')
                e.grid(row=r, column=c, padx=5, pady=0, sticky=tk.W)
                row_entries.append(e)
                if c==1:
                    e.bind("<FocusOut>", self.update_sum)
                    e.bind("<Return>", self.update_sum )

            self.entries.append(row_entries)

        self.line2Lbl = tk.Label(self.dataFrame, text="2  Add the amounts on line 1 . . . . . . . . . ", 
                                 justify='left', font=SMALL_FONT)
        self.line2Lbl.grid(column=0, row=rows+1, sticky=tk.NW)
        #self.line2Text is defined above.  It needed to be assigned before the function call to the function that modified it.
        self.line2Data = tk.Label(self.dataFrame, textvariable=self.line2Text, justify='right', relief=tk.FLAT,
                                  padx=5, width=13, bg='lightgray', font=SMALL_FONT)
        self.line2Data.grid(column=1, row=rows+1)

        self.line3Lbl = tk.Label(self.dataFrame, text="3   Excludable interest on series EE and " \
                                "I U.S. savings bonds issued after 1989 Attach Form 8815.....", font=SMALL_FONT, 
                                wraplength=375, justify="left")
        self.line3Lbl.grid(column=0, row=rows+2, sticky=tk.W)
        self.line3Text = tk.StringVar(value="0")
        self.line3Entry = tk.Entry(self.dataFrame, textvariable=self.line3Text, width=15, justify="right")
        self.line3Entry.grid(column=1, row=rows+2, padx=4,pady=0)
        self.line3Entry.bind("<FocusOut>", self.update_sum)
        self.line3Entry.bind("<Return>", self.update_sum )

        self.line4Lbl = tk.Label(self.dataFrame, text="4  Subtract line 3 from line 2. " \
                                 "Enter the result here and on Form 1040 or 1040-SR, line 2b"\
                                    " if over $1,500 complete part III", font=SMALL_FONT,
                                    wraplength=375, justify="left")
        self.line4Lbl.grid(column=0, row=rows+3, sticky=tk.W)
        self.line4Text = tk.StringVar(value="0")
        self.line4Data = tk.Label(self.dataFrame, textvariable=self.line4Text, justify="right",
                                  relief=tk.FLAT, width=13, bg='lightgray', padx=5, font=SMALL_FONT)
        self.line4Data.grid(column=1, row=rows+3)


        #  *****************   This is PART II of that form *************************************************************
        self.lblPart2 = tk.Label(self.leftFrame, text="Part II ordinary dividends", padx=0,pady=10)
        self.lblPart2.grid(column=0,row=2, sticky=tk.N)
        self.lblP2note = tk.Label(self.leftFrame, font=SMALL_FONT, text="(See instructions "\
                        "and the Instructions for Form 1040, line 3b.) Note: If you received a" \
                        "Form 1099-DIV or substitute statement from a brokerage firm, "\
                        "list the firm’s name as the payer and enter the ordinary " \
                        "dividends shown on that form.", wraplength=85)
        self.lblP2note.grid(column=0, row=3)

        self.lblLine5 = tk.Label(self.dataFrame, text="Enter Line 5 Payers and Amounts below: .........", font=SMALL_FONT)
        self.lblLine5.grid(column=0, row=rows+4, sticky=tk.W+tk.N)
        self.line6Text = tk.StringVar(value=0)
        row_start = rows+5  #need to include this row
        row_end = row_start + 10
        self.part2_entries=[]

        for r in range(row_start, row_end):
            row_entries = []
            for c in range(cols):
                if c == 0:
                    w=60
                else:
                    w=15

                e = tk.Entry(self.dataFrame, width=w, font='Arial, 7')
                e.grid(row=r, column=c, padx=5, pady=0, sticky=tk.W)
                row_entries.append(e)
                if c==1:
                    e.bind("<FocusOut>", self.update_sum_part2)
                    e.bind("<Return>", self.update_sum_part2 )

            self.part2_entries.append(row_entries)
        
        self.line6Lbl = tk.Label(self.dataFrame, text="6  Add the amounts on line 5  If over $1,500 you must complete Part III. . . ", 
                                 justify='left', font=SMALL_FONT)
        self.line6Lbl.grid(column=0, row=row_end+1, sticky=tk.NW )
        #self.line6Text is defined above.  It needed to be assigned before the function call to the function that modified it.
        self.line6Data = tk.Label(self.dataFrame, textvariable=self.line6Text, justify='right', relief=tk.FLAT,
                                  padx=5, width=13, bg='lightgray', font=SMALL_FONT)
        self.line6Data.grid(column=1, row=row_end+1)

        ##   ***************    End Part II   Start Part III ***********************************************************
        
        self.lblPart3 = tk.Label(self.leftFrame, text="Part III Foreign Accounts and Trusts", padx=0,pady=15)
        self.lblPart3.grid(column=0,row=4)

        self.lblPart3note=tk.Label(self.leftFrame, font=SMALL_FONT, text="**CAUTION**: If required, failure to file FinCEN " \
                                   "Form 114 may result in substantial penalties. " \
                                    "Additionally, you may be required to file Form 8938, Statement of Specified " \
                                        "Foreign Financial Assets. See instructions" , wraplength=85 )
        self.lblPart3note.grid(column=0, row=5)

        ### ******************** end part III
        self.lblPart3_header = tk.Label(self.dataFrame, text= "Part III - You must complete this part if you (a) had over $1,500 "\
                                        "of taxable interest or ordinary dividends; (b) had a foreign "\
                                        "account; or (c) received a distribution from, or were a grantor "\
                                            "of, or a transferor to, a foreign trust.", wraplength=500, font='Arial 6')
        self.lblPart3_header.grid(column=0, columnspan=2, row=row_end+2, pady=4, sticky=tk.NW)

        self.lblLine7a = tk.Label(self.dataFrame, font=SMALL_FONT, text=" 7a. At any time during 2025, did you have a financial "\
                                  "interest in or signature authority over a financial "\
                                    "account (such as a bank account, securities account, or brokerage account) "\
                                     "located in a foreign country? See instructions", wraplength=400, justify="left")
        self.lblLine7a.grid(column=0, row=row_end+3, sticky=tk.NW)
        self.varLine7a_1 = tk.IntVar()
        self.cb7a_1 = tk.Checkbutton(self.dataFrame, variable= self.varLine7a_1)
        self.cb7a_1.grid(column=1, row=row_end+3)

        self.lblLine7a_2 = tk.Label(self.dataFrame, font=SMALL_FONT, text=" ... If Yes, are you required to file FinCEN Form 114, "\
                                    "Report of Foreign Bank and Financial Accounts (FBAR), to report that financial interest "\
                                    "or signature authority?  See applicable instructions", 
                                     wraplength=400, justify="left")
        self.lblLine7a_2.grid(column=0, row=row_end+4, sticky=tk.NW)
        self.varLine7a_2 = tk.IntVar()
        self.cbLine7a_2 = tk.Checkbutton(self.dataFrame, variable= self.varLine7a_2)
        self.cbLine7a_2.grid(column=1, row=row_end+4)
        self.lblLine7b = tk.Label(self.dataFrame, font=SMALL_FONT, text="If you are required to file FinCEN Form 114, list the name(s) "\
                                  "of the foreign country(-ies) where the financial account(s) is (are) located:", 
                                  wraplength=400)
        self.lblLine7b.grid(column=0, row=row_end+5)
        self.varLine7b = tk.StringVar()
        self.dataLine7b = tk.Entry(self.dataFrame, textvariable=self.varLine7b, width=75)
        self.dataLine7b.grid(column=0, row=row_end+6, columnspan=2, sticky=tk.NW)

        self.lblLine8 = tk.Label(self.dataFrame, font=SMALL_FONT, text="During 2025, did you receive a distribution from, or were you "\
                                 "the grantor of, or transferor to, a foreign trust? If Yes, you may have to file Form 3520. "\
                                    "See instructions .", wraplength=400, justify="left")
        self.lblLine8.grid(column=0, row=row_end+7, sticky=tk.NW)
        self.varLine8 = tk.IntVar()
        self.cbLine8 = tk.Checkbutton(self.dataFrame, variable= self.varLine8)
        self.cbLine8.grid(column=1, row=row_end+7)

        ##################################    End Part III **********************************************###
        self.btnFrameA =tk.Button(self.leftFrame, text="Frame A", 
                         command=lambda: controller.show_frame("FrameA"))
        self.btnFrameA.grid(column=0, row=6)
        
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

        # Update the label text
        self.line2Text.set(f"Total: {total}")
        try:
            xbonds = float(self.line3Text.get())
            self.line4Text.set(f"Line 4: {total - xbonds}")
        except ValueError:
            pass
    
            #  function to sum part II
    def update_sum_part2(self, event):
        total = 0
        #self.entries is the entire grid.  Return one row at a time
        for rowEntry in self.part2_entries:
            for entry in rowEntry:
                try:
                    # Get text from each entry and convert to float
                    val = float(entry.get())
                    total += val
                except ValueError:
                    # Ignore empty or non-numeric inputs
                    pass

        # Update the label text
        self.line6Text.set(f"Total: {total}")
        """
        try:
            xbonds = float(self.line3Text.get())
            self.line4Text.set(f"Line 4: {total - xbonds}")
        except ValueError:
            pass
        """





