# main.py
import tkinter as tk
from FrameA import FrameA
from FrameB import FrameB

class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        self.frames = {}
        # Initialize frames from different files
        for F in (FrameA, FrameB):
            page_name=F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("FrameA")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update_data(self, text, target_frame):
        #self.frames[target_frame].label.config(text=text)
        frame = self.frames[target_frame]
        frame.label.config(text=text)
        frame.tkraise()





if __name__ == "__main__":
    app = TestApp()
    app.mainloop()   

