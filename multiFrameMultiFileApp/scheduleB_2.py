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

class ScheduleB_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

       


        self.leftFrame = tk.Frame(self, padx=0, pady=0)
        self.leftFrame.grid(column=0, row=0, rowspan=2, sticky=tk.N)

     

        
        

        #use this frame for header labels
        self.headerFrame = tk.Frame(self, padx=0, pady=0)
        self.headerFrame.grid(column=1, row=0, sticky=tk.W+tk.N)
        
     

        #data table frame
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(column=1, row=1, sticky=tk.W+tk.N)
        
        
       

        #  *****************   This is PART II of that form *************************************************************
        self.lblPart2 = tk.Label(self.leftFrame, text="Part II ordinary dividends", padx=0,pady=10)
        self.lblPart2.grid(column=0,row=0, sticky=tk.N)
        self.lblP2note = tk.Label(self.leftFrame, font=SMALL_FONT, text="(See instructions "\
                        "and the Instructions for Form 1040, line 3b.) Note: If you received a" \
                        "Form 1099-DIV or substitute statement from a brokerage firm, "\
                        "list the firm’s name as the payer and enter the ordinary " \
                        "dividends shown on that form.", wraplength=85)
        self.lblP2note.grid(column=0, row=1)

        self.lblLine5 = tk.Label(self.dataFrame, text="Enter Line 5 Payers and Amounts below: .........", font=SMALL_FONT)
        self.lblLine5.grid(column=0, row=2, sticky=tk.W+tk.N)
        self.line6Text = tk.StringVar(value='0')

        cols = 2
        row_start = 3 #need to include this row
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
        



        


        self.btnFrameA =tk.Button(self.leftFrame, text="ScheduleB_3", 
                         command=lambda: controller.show_frame("ScheduleB_3"))
        self.btnFrameA.grid(column=0, row=6)
        
    
    
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





