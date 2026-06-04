import tkinter as tk


class dependents(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.instances = []

        self.entries={}
        self.GridFrame={}

        self.subFrame = tk.Frame(self)
        self.subFrame.pack()
        self.gridFrame0 = tk.Frame(self.subFrame)
        self.gridFrame0.grid(column=0,row=0)
        self.gridFrame1 = tk.Frame(self.subFrame)
        self.gridFrame1.grid(column=1, row=0)
        self.gridFrame2 = tk.Frame(self.subFrame)
        self.gridFrame2.grid(column=2, row=0)
        self.gridFrame3 = tk.Frame(self.subFrame )
        self.gridFrame3.grid(column=3, row=0)
        
        self.GridFrame[0] = self.gridFrame0
        self.GridFrame[1] = self.gridFrame1
        self.GridFrame[2] = self.gridFrame2
        self.GridFrame[3] = self.gridFrame3




        # Create the duplicated frames
        for i in range(4):
            self.create_duplicate_frame(self.GridFrame[i], f"Dependent {i+1}")

        self.btn = tk.Button(self, text="Print Instances",
                             command=self.print_data)
        self.btn.pack(side="right")
        


    def create_duplicate_frame(self, dataFrame, label_text):
        
        
        self.dependentNumber = tk.Label(dataFrame, text=label_text)
        self.dependentNumber.pack()

        self.varLastName = tk.StringVar()
        self.LastName = tk.Entry(dataFrame, textvariable=self.varLastName)
        self.LastName.pack()
        self.handle_placeholder(self.LastName, "Last Name")

        self.varFirstName = tk.StringVar()
        self.FirstName = tk.Entry(dataFrame, textvariable=self.varFirstName)
        self.FirstName.pack()
        self.handle_placeholder(self.FirstName, "First Name")

        self.varSSN = tk.StringVar()
        self.SSN = tk.Entry(dataFrame, textvariable=self.varSSN)
        self.SSN.pack()
        self.handle_placeholder(self.SSN, "Enter SSN")

        self.varRelationship = tk.StringVar()
        self.Relationship = tk.Entry(dataFrame, textvariable=self.varRelationship)
        self.Relationship.pack()
        self.handle_placeholder(self.Relationship, "Relationship")

        # Using the year below should be converted to a variable/dyanamic string
        # ********************************************
        self.varLiveWithYou = tk.IntVar()
        self.chkLiveWithYou = tk.Checkbutton(dataFrame, variable=self.varLiveWithYou, 
                                             text="Check if lived with you more than half of 2025",
                                             wraplength=140)
        self.chkLiveWithYou.pack() # was side=tk.LEFT

        self.varInUSA = tk.IntVar()
        self.chkInUSA = tk.Checkbutton(dataFrame, variable=self.varInUSA, text="And in USA",
                                        wraplength=140)
        self.chkInUSA.pack()

        self.varFullTimeStudent = tk.IntVar()
        self.chkFullTimeStudent = tk.Checkbutton(dataFrame, variable=self.varFullTimeStudent, 
                                                 text="Full time student",
                                                 wraplength=140)
        self.chkFullTimeStudent.pack()

        self.varDisabled = tk.IntVar()
        self.chkDisabled = tk.Checkbutton(dataFrame, variable=self.varDisabled, 
                                          text="Permanently and totally disabled?",
                                          wraplength=140)
        self.chkDisabled.pack()

        #child tax credit
        self.varChildTaxCredit = tk.IntVar()
        self.chkChildTaxCredit = tk.Checkbutton(dataFrame, variable=self.varChildTaxCredit, 
                                                text="Child Tax Credit",
                                                wraplength=140)
        self.chkChildTaxCredit.pack()

        #credit for other dependents
        self.varCreditOtherDependents = tk.IntVar()
        self.chkCreditOtherDependents = tk.Checkbutton(dataFrame, variable=self.varCreditOtherDependents,
                                                       text="Credit for Other Dependents",
                                                       wraplength=140)
        self.chkCreditOtherDependents.pack()

        # store the data for later use
        self.instances.append({
            "DependentNumber": label_text,
            "LastName": self.varLastName,
            "FirstName" : self.FirstName,
            "Relationship" : self.Relationship,
            "SSN" : self.SSN,
            "LiveWithYou" : self.varLiveWithYou,
            "InUSA": self.varInUSA.get(),
            "FullTimeStudent": self.varFullTimeStudent.get(),
            "Disabled" : self.varDisabled.get()

        })
        
    def handle_placeholder(self, entry, placeholder):
        # Set initial state
        entry.insert(0, placeholder)
        entry.config(fg='gray')

        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg='black')

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(fg='gray')

        # Bind the specific entry
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)

    def print_data(self):
        print(self.instances)
