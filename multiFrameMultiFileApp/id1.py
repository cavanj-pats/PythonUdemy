# FrameA.py
import tkinter as tk
#from FrameB import FrameB

SMALL_FONT = ("Arial", 7)

class id1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entries={}

        #  change this to populate a parent window label
        self.label = tk.Label(self, text="Frame A")
        self.label.grid(column=0, row=0, columnspan=3, sticky=tk.W)


        
        #First Name and Middle Initial.  takes up two rows
        self.var_fname = tk.StringVar()

        self.fname = tk.Entry(self, textvariable=self.var_fname)
           
        self.fname.grid(column=0, row=1, stick=tk.W+tk.E)

        self.handle_placeholder(self.fname, "Your first Name, Middle Initial")

        self.entries["fname"] = self.fname  #i don't know if this is necessary


        self.var_lname = tk.StringVar()
        
        self.lname = tk.Entry(
            self, 
            textvariable=self.var_lname
            )
        
        self.lname.grid(column=1, row=1, sticky=tk.W+tk.E)
        self.entries["lname"] = self.lname
        self.handle_placeholder(self.lname, "Your Last Name")
        
        self.var_socsec = tk.StringVar()
        
        self.socsec = tk.Entry(
            self, 
            textvariable=self.var_socsec, 
            width=12)
        self.socsec.grid(column=2, row=1, sticky=tk.W+tk.E)
        self.entries["socsec"] = self.socsec
        self.handle_placeholder(self.socsec, "Your SSN")
        
        #Spouse First name and middle initial
        self.var_sfname = tk.StringVar()
        
        self.sfname = tk.Entry(
            self, 
            textvariable=self.var_sfname
            )
        self.sfname.grid(column=0, row= 2,  sticky=tk.W+tk.E)     
        self.entries["sfname"] = self.sfname
        self.handle_placeholder(self.sfname, "Spouse First Name, Middle Initial")


        self.var_slname = tk.StringVar()
        
        self.slname = tk.Entry(
            self, 
            textvariable=self.var_slname
            )
        
        self.slname.grid(column=1, row=2,  sticky=tk.W+tk.E)
        
        self.entries["slname"] = self.slname
        
        self.handle_placeholder(self.slname, "Spouse Last Name")


        self.var_ssocsec = tk.StringVar()
    
        self.ssocsec = tk.Entry(self, textvariable=self.var_ssocsec, width=12)
        
        self.ssocsec.grid(column=2, row=2, sticky=tk.W+tk.E)
        self.entries["ssocsec"]= self.ssocsec
        self.handle_placeholder(self.ssocsec, "Spouse SSN")


        self.varHomeAddress = tk.StringVar()
        self.lblHomeAddress = tk.Label(
            self, 
            text='Home address number and street. If you have a P.O. box see instructions.',
            justify=tk.LEFT
                        )
        
        self.lblHomeAddress.grid(column=0, row=3, columnspan=3, sticky=tk.W)

        self.HomeAddress = tk.Entry(
            self, 
            textvariable=self.varHomeAddress
            )
        
        self.HomeAddress.grid(column=0, row=4, sticky=tk.W+tk.E)

        self.entries["HomeAddress"] = self.HomeAddress
        self.handle_placeholder(self.HomeAddress, "Home Address Number and Street.")


        self.varAptNum = tk.StringVar()
      
        self.AptNum = tk.Entry(
            self, 
            textvariable=self.varAptNum
            )
        self.AptNum.grid(column=1, row=4, sticky=tk.W+tk.E)
        self.entries["AptNum"]= self.AptNum
        self.handle_placeholder(self.AptNum, "Apartment Number")

        #this can actually be put at the bottom
        self.varIntMainHome = tk.IntVar(value=0)
        self.lblMainHome = tk.Label(self, text="Check here if your main home, and your spouses if filing a joint return, was in the" \
                                            "U.S. for more than half of 2025",
                                            font='Arial, 8')
        self.lblMainHome.grid(column=0, row=5, columnspan=3,rowspan=2, sticky=tk.W+tk.N)
        self.chkMainHome = tk.Checkbutton(
            self, 
            variable=self.varIntMainHome
            )
        self.chkMainHome.grid(column=1, row=7, sticky=tk.E)
        self.entries["MainHome"] = self.varIntMainHome   #put the variable data value.  so later function can use .get()


        self.varCity = tk.StringVar()
        self.lblCity = tk.Label(self, text="City, town, or post office. If you have a foreign address" \
                                ",also complete spaces below. ", 
                                font='Arial, 8')
        self.lblCity.grid(column=0, row=8, columnspan=3, rowspan=2, sticky=tk.NSEW)
        self.City = tk.Entry(
            self, 
            textvariable=self.varCity
            )
        self.City.grid(column=0, row=10, sticky=tk.W+tk.E)
        self.entries["City"]= self.City
        self.handle_placeholder(self.City, "Enter City/Town")
        
        
        
        self.varState = tk.StringVar()

        self.state = tk.Entry(
            self, 
            textvariable=self.varState, 
            width=5
            )
        self.state.grid(column=1, row=10, sticky=tk.W+tk.E)
        self.entries["state"] = self.state
        self.handle_placeholder(self.state, "State")

        self.varZip=tk.StringVar()
  
        self.zip = tk.Entry(
            self, 
            textvariable=self.varZip
            )
        self.zip.grid(column=2, row=10, sticky=tk.W+tk.E)
        self.entries["zip"]= self.zip
        self.handle_placeholder(self.zip,"Zip Code")

        #need to add:
        #Foreign country name 
        self.varFcountry=tk.StringVar()
        self.f_country=tk.Entry(
            self,
            textvariable=self.varFcountry
        )
        self.f_country.grid(column=0, row=11, sticky=tk.W+tk.E)
        self.handle_placeholder(self.f_country, "Foreign Country Name")

        # Foreign province/state/county 
        self.varFprov=tk.StringVar()
        self.f_prov = tk.Entry(
            self,
            textvariable=self.varFprov
        )
        self.f_prov.grid(column=1, row=11, sticky=tk.W+tk.E)
        self.handle_placeholder(self.f_prov, "Foreign Province, State, County")

        # Foreign postal code
        self.varFpostal=tk.StringVar()
        self.f_postal=tk.Entry(
            self,
            textvariable=self.varFpostal
        )
        self.f_postal.grid(column=2, row=11, sticky=tk.W+tk.E)
        self.handle_placeholder(self.f_postal, "Foreign Postal Code")
        
    


        """
        

        self.btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame("FrameB") )  #Example logic
        self.btn.grid(column=5, row=srow+15, columnspan=2)

        label_line11_income=tk.Label(self)
        label_line11_income.grid(column=4, row=0, columnspan=3)  #put result of calculation here
        
        
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