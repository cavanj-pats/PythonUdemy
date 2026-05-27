import tkinter as tk


class dependents(tk.Frame):
    def __init__(self, parent, controller):


        self.entries={}
        self.LastName = tk.Entry(self)

        self.FirstName = tk.Entry(self)

        self.SSN = tk.Entry(self)

        self.Relationship = tk.Entry(self)

        self.chkLiveWithYou = tk.Checkbutton(self)
        
        self.chkLivedInUSA = tk.Checkbutton(self)

        self.chkFullTimeStudent=tk.Checkbutton(self)

        self.chkDisabled = tk.Checkbutton(self)

        self.chkChildTaxCredit = tk.Checkbutton(self)

        self.chkOtherDependents = tk.Checkbutton(self)
        
