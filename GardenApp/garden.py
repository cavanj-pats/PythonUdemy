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




class fuelMix(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)















if __name__ == "__main__":
    app = gardenApp()
    app.mainloop()  