#w2.py
#i dont know if this will be one W2 or if it will be all applicable w2's

#need to add functionality for mnore than one W2 to be created.

import tkinter as tk

SMALL_FONT = ("Arial", 8)

class W2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Register the validation function
        vcmd = (parent.register(self.validate_numeric), '%P', '%W')

        self.instance_id = 0   #index each time you save and clear form to start a new instance
        self.label = tk.Label(self, text="W2")
        self.label.grid(column=0, row=0, columnspan=2)

        self.dataValidate = tk.Label(self, text="")
        self.dataValidate.grid(column=2, row=0, columnspan=2, sticky=tk.W)
        
        self.lblbox1 = tk.Label(self, text="1 Wages", font=SMALL_FONT)
        self.lblbox1.grid(column=0, row=2, columnspan=3)
        self.varBox1 = tk.StringVar() #will need to convert to float
        self.Box1 = tk.Entry(self, validatecommand=vcmd, 
                             validate="focusout", textvariable=self.varBox1, 
                             justify=tk.RIGHT, name='_Box1')
        self.Box1.grid(column=0, row=3, columnspan=3)

        self.lblbox2 = tk.Label(self, text='Fed Income Tax Witheld', font=SMALL_FONT )
        self.lblbox2.grid(column=3, row=2, columnspan=3)
        varBox2 = tk.StringVar()
        self.Box2 = tk.Entry(self, textvariable=varBox2, name='_Box2')
        self.Box2.grid(column=3, row=3, columnspan=3)

        self.varBox3 = tk.StringVar()
        self.lblBox3 = tk.Label(self, text='Soc Sec Wages', font=SMALL_FONT)
        self.lblBox3.grid(column=0, row=4, columnspan=3)
        self.Box3 = tk.Entry(self, textvariable=self.varBox3, name='_Box3' )
        self.Box3.grid(column=0, row=5, columnspan=3)

        self.varBox4 = tk.StringVar()
        self.lblBox4 = tk.Label(self, text='Soc Sec Tax Wintheld', font=SMALL_FONT)
        self.lblBox4.grid(column=3, row=4, columnspan=3)
        self.Box4 = tk.Entry(self, textvariable=self.varBox4, name='_Box4' )
        self.Box4.grid(column=3, row=5, columnspan=3)

        self.varBox5 = tk.StringVar()
        self.lblBox5 = tk.Label(self, text='Medicare Wages', font=SMALL_FONT)
        self.lblBox5.grid(column=0, row=6, columnspan=3)
        self.Box5 = tk.Entry(self, textvariable=self.varBox5, name='_Box5' )
        self.Box5.grid(column=0, row=7, columnspan=3)

        self.varBox6 = tk.StringVar()
        self.lblBox6 = tk.Label(self, text='Medicare Tax Witheld', font=SMALL_FONT)
        self.lblBox6.grid(column=3, row=6, columnspan=3)
        self.Box6 = tk.Entry(self, textvariable=self.varBox6, name='_Box6' )
        self.Box6.grid(column=3, row=7, columnspan=3)

        self.varBoxd = tk.StringVar()
        self.lblBoxd = tk.Label(self, text='Control Number', font=SMALL_FONT)
        self.lblBoxd.grid(column=0, row=8, columnspan=3)
        self.Boxd = tk.Entry(self, textvariable=self.varBoxd, name='_Boxd' )
        self.Boxd.grid(column=0, row=9, columnspan=3)

        self.varBoxb = tk.StringVar()
        self.lblBoxb = tk.Label(self, text='Employers Fed ID Number', font=SMALL_FONT)
        self.lblBoxb.grid(column=0, row=10, columnspan=3)
        self.Boxb = tk.Entry(self, textvariable=self.varBoxb, name='_Boxb' )
        self.Boxb.grid(column=0, row=11, columnspan=3)

        self.varBoxa = tk.StringVar()
        self.lblBoxa = tk.Label(self, text='Employee SSA number', font=SMALL_FONT)
        self.lblBoxa.grid(column=3, row=10, columnspan=3)
        self.Boxa = tk.Entry(self, textvariable=self.varBoxa, name='_Boxa' )
        self.Boxa.grid(column=3, row=11, columnspan=3)

        self.varBox7 = tk.StringVar()
        self.lblBox7 = tk.Label(self, text='Soc Sec Tips', font=SMALL_FONT)
        self.lblBox7.grid(column=0, row=12, columnspan=3)
        self.Box7 = tk.Entry(self, textvariable=self.varBox7, name='_Box7' )
        self.Box7.grid(column=0, row=13, columnspan=3)

        self.varBox8 = tk.StringVar()
        self.lblBox8 = tk.Label(self, text='Allocated Tips', font=SMALL_FONT)
        self.lblBox8.grid(column=3, row=12, columnspan=3)
        self.Box8 = tk.Entry(self, textvariable=self.varBox8, name='_Box8' )
        self.Box8.grid(column=3, row=13, columnspan=3)
        
        self.varBox9 = tk.StringVar()
        self.lblBox9 = tk.Label(self, text='9', font=SMALL_FONT)
        self.lblBox9.grid(column=0, row=14, columnspan=3)
        self.Box9 = tk.Entry(self, textvariable=self.varBox9, name='_Box9' )
        self.Box9.grid(column=0, row=15, columnspan=3)
        
        self.varBox10 = tk.StringVar()
        self.lblBox10 = tk.Label(self, text='Dep Care Benefits', font=SMALL_FONT)
        self.lblBox10.grid(column=3, row=14, columnspan=3)
        self.Box10 = tk.Entry(self, textvariable=self.varBox10, name='_Box10' )
        self.Box10.grid(column=3, row=15, columnspan=3)

        self.varBox11 = tk.StringVar()
        self.lblBox11 = tk.Label(self, text='Non qualfied plans', font=SMALL_FONT)
        self.lblBox11.grid(column=0, row=16, columnspan=3)
        self.Box11 = tk.Entry(self, textvariable=self.varBox11, name='_Box11' )
        self.Box11.grid(column=0, row=17, columnspan=3)

        self.varBox12a_code = tk.StringVar()
        self.lblBox12a_code = tk.Label(self, text='12a', font=SMALL_FONT)
        self.lblBox12a_code.grid(column=3, row=16, columnspan=1)
        self.Box12a_code = tk.Entry(self, textvariable=self.varBox12a_code, name='_Box12a_code', width=4 )
        self.Box12a_code.grid(column=3, row=17, columnspan=1)

        self.varBox12a_data = tk.StringVar()
        #self.lblBox12a_data = tk.Label(self, text=' ', font=SMALL_FONT)
        #self.lblBox12a_data.pack()
        self.Box12a_data = tk.Entry(self, textvariable=self.varBox12a_data, name='_Box12a_data', width=12 )
        self.Box12a_data.grid(column=4, row=17, columnspan=2)

        self.varBox12b_code = tk.StringVar()
        self.lblBox12b_code = tk.Label(self, text='12b', font=SMALL_FONT)
        self.lblBox12b_code.grid(column=3, row=18, columnspan=1)
        self.Box12b_code = tk.Entry(self, textvariable=self.varBox12b_code, name='_Box12b_code', width=4 )
        self.Box12b_code.grid(column=3, row=19, columnspan=1)

        self.varBox12b_data = tk.StringVar()
        #self.lblBox12b_data = tk.Label(self, text=' ', font=SMALL_FONT)
        #self.lblBox12b_data.pack()
        self.Box12b_data = tk.Entry(self, textvariable=self.varBox12b_data, name='_Box12b_data', width=12 )
        self.Box12b_data.grid(column=4, row=19, columnspan=2)

        self.varBox12c_code = tk.StringVar()
        self.lblBox12c_code = tk.Label(self, text='12c', font=SMALL_FONT)
        self.lblBox12c_code.grid(column=3, row=20, columnspan=1)
        self.Box12c_code = tk.Entry(self, textvariable=self.varBox12c_code, name='_Box12c_code', width=4 )
        self.Box12c_code.grid(column=3, row=21, columnspan=1)

        self.varBox12c_data = tk.StringVar()
        #self.lblBox12c_data = tk.Label(self, text=' ', font=SMALL_FONT)
        #self.lblBox12c_data.pack()
        self.Box12c_data = tk.Entry(self, textvariable=self.varBox12c_data, name='_Box12c_data', width=12 )
        self.Box12c_data.grid(column=4, row=21, columnspan=2)

        self.varBox12d_code = tk.StringVar()
        self.lblBox12d_code = tk.Label(self, text='12d', font=SMALL_FONT)
        self.lblBox12d_code.grid(column=3, row=22, columnspan=3, sticky=tk.W)
        self.Box12d_code = tk.Entry(self, textvariable=self.varBox12d_code, name='_Box12d_code', width=4 )
        self.Box12d_code.grid(column=3, row=23, columnspan=1)

        self.varBox12d_data = tk.StringVar()
        #self.lblBox12d_data = tk.Label(self, text=' ', font=SMALL_FONT)
        #self.lblBox12d_data.pack()
        self.Box12d_data = tk.Entry(self, textvariable=self.varBox12d_data, name='_Box12d_data', width=12 )
        self.Box12d_data.grid(column=4, row=23, columnspan=2, sticky=tk.E+tk.W)

        self.varBox15 = tk.StringVar()
        self.lblBox15 = tk.Label(self, text='State', font=SMALL_FONT)
        self.lblBox15.grid(column=0, row=24, columnspan=1)
        self.Box15 = tk.Entry(self, textvariable=self.varBox15, name='_Box15' )
        self.Box15.grid(column=0, row=25, columnspan=1)

        self.varBoxStateID = tk.StringVar()
        self.lblBoxStateID = tk.Label(self, text='Employers State ID', font=SMALL_FONT)
        self.lblBoxStateID.grid(column=1, row=24, columnspan=2)
        self.BoxStateID = tk.Entry(self, textvariable=self.varBoxStateID, name='_BoxStateID' )
        self.BoxStateID.grid(column=1, row=25, columnspan=2)

        self.varBox16 = tk.StringVar()
        self.lblBox16 = tk.Label(self, text='State Wages, Tips, etc.', font=SMALL_FONT)
        self.lblBox16.grid(column=3, row=24, columnspan=3)
        self.Box16 = tk.Entry(self, textvariable=self.varBox16, name='_Box16' )
        self.Box16.grid(column=3, row=25, columnspan=3)

        self.varBox17 = tk.StringVar()
        self.lblBox17 = tk.Label(self, text='State Income Tax', font=SMALL_FONT)
        self.lblBox17.grid(column=0, row=26, columnspan=3)
        self.Box17 = tk.Entry(self, textvariable=self.varBox17, name='_Box17' )
        self.Box17.grid(column=0, row=27, columnspan=3)

        self.varBox18 = tk.StringVar()
        self.lblBox18 = tk.Label(self, text='Local Wages, tips, etc', font=SMALL_FONT)
        self.lblBox18.grid(column=3, row=26, columnspan=3)
        self.Box18 = tk.Entry(self, textvariable=self.varBox18, name='_Box18' )
        self.Box18.grid(column=3, row=27, columnspan=3)

        self.varBox19 = tk.StringVar()
        self.lblBox19 = tk.Label(self, text='Local Income Tax', font=SMALL_FONT)
        self.lblBox19.grid(column=0, row=28, columnspan=3)
        self.Box19 = tk.Entry(self, textvariable=self.varBox19, name='_Box19' )
        self.Box19.grid(column=0, row=29, columnspan=3)

        self.varBox20 = tk.StringVar()
        self.lblBox20 = tk.Label(self, text='Locality Name', font=SMALL_FONT)
        self.lblBox20.grid(column=3, row=28, columnspan=3)
        self.Box20 = tk.Entry(self, textvariable=self.varBox20, name='_Box20' )
        self.Box20.grid(column=3, row=29, columnspan=3)

        
        btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame("FrameB") ) 
        btn.grid(column=2, row=30, columnspan=3)
        btnW2 =tk.Button(self, text="Next W2 Form", 
                         command=lambda: controller.create_new_instance(W2))
        btnW2.grid(column=2, row=31, columnspan=3)
        btnSave = tk.Button(self, text="Save Data", command=self.save_data)
        btnSave.grid(column=2, row=32, columnspan=3)
        #all other controls and functionality go here
        """
            box 1 wages
            box 2 fed income tax witheld
            3 soc sec wages
            4 soc sec tax witheld
            6 medicare tax witheld
            d control number.   text
            c employer.     text
            b employer fed id number.  text
            a employee soc sec number.  text
            12a.  code and value. code is text value is numeric
            12b.   code and value
            12c
            12d
            13 stat emp. ret plan.  3rd party sick pay. checkboxes
            15.  state
            16 state wages tips
            17 state income tax

            figure out a stack of the previous frame or window

        """
    def save_data(self):
        entry_data = {}
        entry_data['instance_id']=self.instance_id
        
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                if widget.get() != "":
                    entry_data[str(widget).split('_')[-1]] = float(widget.get())
                else:
                    entry_data[str(widget).split('_')[-1]] = 0
            
        print("Saved W2 Data: ", entry_data)
        
        
        #  self.varBox1.set("")  #this works
        self.Box1.delete(0, tk.END)   # this works to clear the data
        self.Box1.insert(0, entry_data['Box1']-10)   #this works to refill the data
        
        
    def validate_numeric(self, proposed_value, W):
        # Allow empty string (for backspacing) or digits only
        widget = self.nametowidget(W)

        print(widget.cget("bg"))
        #on macOS returns systemTextBackgroundColor


        if proposed_value == "" or proposed_value.isdigit():
            self.dataValidate.config(text='good')
            self.dataValidate.config(fg='black')
            widget.config(bg='systemTextBackgroundColor')  #i don't know if this will work on windows or linux
            return True


        self.dataValidate.config(text='Bad Data')
        self.dataValidate.config(fg='red')
        widget.config(bg='red')
        return True  #return True either way so as to not switch off validation
       