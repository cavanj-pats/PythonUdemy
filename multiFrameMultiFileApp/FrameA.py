# FrameA.py
import tkinter as tk
#from FrameB import FrameB

class FrameA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Frame A")
        self.label.pack()

        


        self.btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame("FrameB") )  #Example logic
        self.btn.pack()
        label_line11_income=tk.Label(self)
        label_line11_income.pack()  #put result of calculation here