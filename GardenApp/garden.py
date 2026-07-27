#garden.py   app for gardeners, apple growers and two stoke fuel mixers

import tkinter as tk

"""
    1 fl. ounce = 2 tablespoons   tbs
    1 TBS = 3 teaspoons   tsp
    1 cup = 8 fl. ounces
    1 quart = 32 fl. ounces
    1 gallon = 128 fl. ounces

    1 fl. ounce = 29.57 ml
    1 TBS = 14.7 ml


    Spray Mix calculations can be given in ounces or tbs, tsp per gallon 
    when mixing larger or smaller amounts,  the amount of product needs to be
    calculated
"""


"""
    ##################    This app will also provide caclutions for two stroke 
                           fuel and oil mixing
    1) you have a volume of fuel and a desired fuel/oil mixture
    2) you want to know how much oil is required.

    Another option
    1) you have a certain ratio.  You want to change it.
    2) you may need to add oil or add fuel depending on the change.

"""

class gardenApp(tk.Tk):
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # this will be the main app window controlling frames 

        self.mainFrame = tk.Frame(self, bg="light green")
        self.mainFrame.pack()

        self.sprayFrame = sprayCalcs(self, self.mainFrame)
        self.sprayFrame.pack()
        self.sprayFrame.tkraise()



class fuelMix(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #  1) You have fuel amount and desired fuel/oil ratio
        # allow ounces or milliliters

        varFuelAmt = tk.StringVar()
        entFuelAmt = tk.Entry(self, textvariable=varFuelAmt )
        entFuelAmt.pack()

        #add a label of ounces or milliliters and a radio button to toggle

        lstFuelPreMix = tk.Listbox(self)
        lstFuelPreMix.insert(0, "100% Fuel")
        lstFuelPreMix.insert(1, '50:1')
        lstFuelPreMix.insert(2, '40:1')
        lstFuelPreMix.insert(3, '32:1')
        lstFuelPreMix.pack()
        
        # after adding the oil this is what you will have
        lstFuelPostMix = tk.Listbox(self)
        lstFuelPostMix.insert(0, '50:1')
        lstFuelPostMix.insert(1, '40:1')
        lstFuelPostMix.insert(2, '32:1')
        lstFuelPostMix.pack()




    def add_oil(self, volume, concentration):
        #calculated oil to add
        pass

    def add_fuel(self, volume, concentration):
        #calculate fuel to add
        pass

class sprayCalcs(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #other code here
        self.varMixVolume = tk.StringVar()
        self.lblAmount = tk.Label(self, text="Mix: ")
        self.lblAmount.grid(row=0, column=0)
        self.valAmount = tk.Entry(self, textvariable=self.varMixVolume)
        self.valAmount.grid(row=0, column=1)
        self.lstMixUnits = tk.Listbox(self)
        self.lstMixUnits.insert(0,'ounces')
        self.lstMixUnits.insert(1, 'TBS')
        self.lstMixUnits.insert(2,'Gallon')
        self.lstMixUnits.grid(row=0, column=2)

        self.varNameProduct = tk.StringVar()
        self.lblProduct = tk.Label(self, text='Product')
        self.lblProduct.grid(row=1, column=0)
        self.valProduct = tk.Entry(self, textvariable=self.varNameProduct)
        self.valProduct.grid(row=1, column=1)

        self.varMixRate = tk.StringVar()
        self.lblMixRate = tk.Label(self, text='Label Mix Rate: ')
        self.lblMixRate.grid(row=2, column=0)

        self.MixRate = tk.Entry(self, textvariable=self.varMixRate)
        self.MixRate.grid(row=2, column=1)
        
        self.lblProductUnits = tk.Label(self, text='ounces / gallon')
        self.lblProductUnits.grid(row=2, column=2)

        self.btnCalculate=tk.Button(self, text='Calculate', command=self.calculate)
        self.btnCalculate.grid(row=3, column=2)

        self.varResult = tk.StringVar()
        self.result = tk.Entry(self, textvariable=self.varResult)
        self.result.grid(row=4, column=1)

    def calculate(self):
        totalVolume = int(self.varMixVolume.get())
        rate = int(self.varMixRate.get())

        #rate will be ounces per gallon to keep it simple for now

        index = self.lstMixUnits.get(self.lstMixUnits.curselection())

        if index == 'ounces' :
            #totalVolume * rate / 128 ounces per gallong
            self.varResult.set(f"{totalVolume * rate / 128} ounces of product to make {totalVolume} ounces")
        elif index == 1:
            pass
        else:
            pass















if __name__ == "__main__":
    app = gardenApp()
    app.mainloop()  