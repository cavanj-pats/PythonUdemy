import tkinter as tk


class dependents(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entries={}

        self.varLastName = tk.StringVar()
        self.LastName = tk.Entry(self, textvariable=self.varLastName)
        self.LastName.pack()
        self.handle_placeholder(self.LastName, "Last Name")

        self.FirstName = tk.Entry(self)
        self.FirstName.pack()
        self.handle_placeholder(self.FirstName, "First Name")

        self.SSN = tk.Entry(self)
        self.SSN.pack()
        self.handle_placeholder(self.SSN, "Enter SSN")

        self.Relationship = tk.Entry(self)
        self.Relationship.pack()
        self.handle_placeholder(self.Relationship, "Relationship")

        # Using the year below should be converted to a variable/dyanamic string
        # ********************************************
        self.varLiveWithYou = tk.IntVar()
        self.chkLiveWithYou = tk.Checkbutton(self, variable=self.varLiveWithYou, 
                                             text="Check if lived with you more than half of 2025",
                                             wraplength=140)
        self.chkLiveWithYou.pack() # was side=tk.LEFT


        #self.label1 = tk.Label(self, text="Check if lived with you more than half 2025", wraplength=15)
        #self.label1.pack(side=tk.LEFT)
        
        """
        self.chkLivedInUSA = tk.Checkbutton(self)

        self.chkFullTimeStudent=tk.Checkbutton(self)

        self.chkDisabled = tk.Checkbutton(self)

        self.chkChildTaxCredit = tk.Checkbutton(self)

        self.chkOtherDependents = tk.Checkbutton(self)
        """


        
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
