# FrameA.py
import tkinter as tk
from FrameB import FrameB

class FrameA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Frame A")
        self.label.pack()
        btn = tk.Button(self, text="Go to B", 
                        command=lambda: controller.show_frame(FrameB) )  #Example logic
        btn.pack()