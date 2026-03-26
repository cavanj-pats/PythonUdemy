


import tkinter as tk
from tkinter import ttk



def joint():
    if varJoint.get() == 1:
        txt_name2.config(state=tk.NORMAL)
        txt_lname2.config(state=tk.NORMAL)
    else:
        txt_name2.config(state=tk.DISABLED)
        txt_lname2.config(state=tk.DISABLED)



root = tk.Tk()
root.title("Tabbed Window")

# Create the Notebook (tab control)
notebook = ttk.Notebook(root)

# Create tab frames
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Pack the notebook to expand and fill the window
notebook.pack(expand=1, fill="both")




# Add content to Tab 1
ttk.Label(tab1, text="Welcome to Tab 1").pack(padx=20, pady=20)

# Add content to Tab 2
ttk.Label(tab2, text="Welcome to Tab 2").pack(padx=20, pady=10)
varJoint = tk.IntVar(value=0) #unchecked
chkJoint = tk.Checkbutton(tab2, variable=varJoint, text='Check if joint return', command=joint)
chkJoint.pack()

#make a frame to hold taxper information
taxPayerFrame = ttk.Frame(tab2)
taxPayerFrame.pack()

##   make tab2 for Taxpayer information
"""
    _name1, _lname1, SS1
    name2, _lName2, SS2
    addr,  apt
    city, town, state, zip
    fornCountryName, fornProvStateCounty, fornPostal
"""
lbl_name1 = ttk.Label(taxPayerFrame, text='Taxpayer First Name and Middle Initial' )
lbl_lname1= ttk.Label(taxPayerFrame, text='Taxpayer Last Name')
lbl_SS1 = ttk.Label(taxPayerFrame, text='Taxpayer Soc. Sec.')
lbl_name1.grid(row=0, column=0, sticky=tk.W+tk.N)
lbl_lname1.grid(row=0, column=1, sticky=tk.W+tk.N)
lbl_SS1.grid(row=0, column=2, sticky=tk.W+tk.N)

txt_name1 = ttk.Entry(taxPayerFrame)
txt_lname1 = ttk.Entry(taxPayerFrame)
txt_SS1 = ttk.Entry(taxPayerFrame)
txt_name1.grid(column=0, row=1, sticky=tk.E+tk.W)
txt_lname1.grid(row=1, column=1, sticky=tk.E+tk.W)
txt_SS1.grid(row=1, column=2, sticky=tk.E+tk.W)

lbl_name2 = ttk.Label(taxPayerFrame,  text='If joint, Spouse First Name and Middle Initial' )
lbl_lname2= ttk.Label(taxPayerFrame, text='Spouse Last Name')
lbl_SS2 = ttk.Label(taxPayerFrame, text='Spouse Soc. Sec.')
lbl_name2.grid(row=2, column=0, sticky=tk.W+tk.N)
lbl_lname2.grid(row=2, column=1, sticky=tk.W+tk.N)
lbl_SS2.grid(row=2, column=2, sticky=tk.W+tk.N)

txt_name2 = ttk.Entry(taxPayerFrame)
txt_lname2 = ttk.Entry(taxPayerFrame)
txt_SS2 = ttk.Entry(taxPayerFrame)
txt_name2.grid(column=0, row=3, sticky=tk.E+tk.W)
txt_lname2.grid(row=3, column=1, sticky=tk.E+tk.W)
txt_SS2.grid(row=3, column=2, sticky=tk.E+tk.W)

lbl_city = ttk.Label(taxPayerFrame, text='City')
lbl_state = ttk.Label(taxPayerFrame, text='State')
lbl_zip = ttk.Label(taxPayerFrame, text='Zip Code')
txt_city = ttk.Entry(taxPayerFrame)
txt_state = ttk.Entry(taxPayerFrame)
txt_zip = ttk.Entry(taxPayerFrame)

lbl_city.grid(row = 4, column=0, sticky=tk.W+tk.N)
lbl_state.grid(row=4, column=1, sticky=tk.W+tk.N)
lbl_zip.grid(row=4, column=2, sticky=tk.W+tk.N)
txt_city.grid(row=5, column=0, sticky=tk.E+tk.W)
txt_state.grid(row=5, column=1, sticky=tk.E+tk.W)
txt_zip.grid(row=5, column=2, sticky=tk.E+tk.W)

joint()



root.mainloop()