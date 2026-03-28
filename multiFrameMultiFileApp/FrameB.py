# FrameB.py
import tkinter as tk
#from FrameA import FrameA

class FrameB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Frame B")
        self.label.pack()
        btn = tk.Button(self, text="Update A", 
                        command=lambda: controller.update_data("Updated!", "FrameA"))
        btn.pack()
        btnW2 =tk.Button(self, text="W2 Form", 
                         command=lambda: controller.show_frame("W2"))
        btnW2.pack()

