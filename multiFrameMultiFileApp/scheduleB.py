#this will be Schedule B Form 1040

import tkinter as tk
#from FrameB import FrameB

SMALL_FONT = ("Arial", 7)




class ScheduleB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.leftFrame = tk.Frame(self, padx=0, pady=0)
        self.leftFrame.grid(column=0, row=0, rowspan=2)

        self.lblPart1 = tk.Label(self.leftFrame, text='Part I interest', padx=0,pady=0)
        self.lblPart1.grid(column=0,row=0)
        self.lblP1note = tk.Label(self.leftFrame, font=SMALL_FONT, text="(See instructions and the Instructions for Form 1040, "\
                                   " line 2b.) Note: If you received a Form 1099-INT, Form 1099-OID, or substitute statement from a brokerage firm, "\
                                    "list the firm’s name as the payer and enter the total interest "\
                                        "shown on that form", wraplength=80)
        self.lblP1note.grid(column=0, row=1)

        """
        self.btnFrameA =tk.Button(self.leftFrame, text="Frame A", 
                         command=lambda: controller.show_frame("FrameA"))
        self.btnFrameA.grid(column=0, row=2)
        """
        

        #use this frame for header labels
        self.headerFrame = tk.Frame(self, padx=0, pady=0)
        self.headerFrame.grid(column=1, row=0, sticky=tk.W)
        
        self.headerLabel = tk.Label(self.headerFrame, text= "1.  List name of payer. If any interest is " \
                                    "from a seller-financed mortgage and the " \
                                    "buyer used the property as a personal residence, " \
                                    "see the instructions and list this interest first. Also, show that "\
                                    "buyer’s social security number and address:",  wraplength=400, 
                                    font=SMALL_FONT, justify='left', padx=5, pady=0)
        
        self.headerLabel.pack()

        #data table frame
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(column=1, row=1)
        
        # i think i need to define the variable here, before i call i function that sets it
        self.line2Text = tk.StringVar(value="0")
        
        rows, cols = 10, 2
        self.entries = []
        

        for r in range(rows):
            row_entries = []
            for c in range(cols):
                if c == 0:
                    w=60
                else:
                    w=15

                e = tk.Entry(self.dataFrame, width=w)
                e.grid(row=r, column=c, padx=5, pady=1)
                row_entries.append(e)
                if c==1:
                    e.bind("<FocusOut>", self.update_sum)
                    e.bind("<Return>", self.update_sum )

            self.entries.append(row_entries)

        self.line2Lbl = tk.Label(self.dataFrame, text="2  Add the amounts on line 1 . . . . . . . . . ", 
                                 justify='left')
        self.line2Lbl.grid(column=0, row=rows+1)
        #self.line2Text = tk.StringVar(value="0")
        self.line2Data = tk.Label(self.dataFrame, textvariable=self.line2Text, justify='right', relief=tk.FLAT,
                                  padx=5, width=13, bg='lightgray')
        self.line2Data.grid(column=1, row=rows+1)

        self.line3Lbl = tk.Label(self.dataFrame, text="3   Excludable interest on series EE and " \
                                "I U.S. savings bonds issued after 1989 Attach Form 8815.....")
        self.line3Lbl.grid(column=0, row=rows+2)
        self.line3Text = tk.StringVar(value="0")
        self.line3Entry = tk.Entry(self.dataFrame, textvariable=self.line3Text, width=15, justify="right")
        self.line3Entry.grid(column=1, row=rows+2, padx=4,pady=5)
        self.line3Entry.bind("<FocusOut>", self.update_sum)
        self.line3Entry.bind("<Return>", self.update_sum )

        self.line4Lbl = tk.Label(self.dataFrame, text="4  Subtract line 3 from line 2. " \
                                 "Enter the result here and on Form 1040 or 1040-SR, line 2b")
        self.line4Lbl.grid(column=0, row=rows+3)
        self.line4Text = tk.StringVar(value="0")
        self.line4Data = tk.Label(self.dataFrame, textvariable=self.line4Text, justify="right",
                                  relief=tk.FLAT, width=13, bg='lightgray', padx=5)
        self.line4Data.grid(column=1, row=rows+3)


        #  *****************   This is PART II of that form *********************
        self.lblPart2 = tk.Label(self.leftFrame, text="Part II ordinary dividents", padx=0,pady=0)
        self.lblPart2.grid(column=0,row=2)
        self.lblP2note = tk.Label(self.leftFrame, font=SMALL_FONT, text="(See instructions "\
                        "and the Instructions for Form 1040, line 3b.) Note: If you received a" \
                        "Form 1099-DIV or substitute statement from a brokerage firm, "\
                        "list the firm’s name as the payer and enter the ordinary " \
                        "dividends shown on that form.", wraplength=80)
        self.lblP2note.grid(column=0, row=3)




        ##   ***************    End Part II

        ##  ********************Part III

        ### ******************** end part III


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
    

       





