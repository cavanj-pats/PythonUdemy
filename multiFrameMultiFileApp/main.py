# main.py
import tkinter as tk
from FrameA import FrameA
from FrameB import FrameB
from w2 import W2

class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        self.frames = {}
        # Initialize frames from different files
        #need a navigation frame
        #ok to use grid just
        navFrame=tk.Frame(container, height=900, width=300, padx=50)
        navFrame.grid(row=0, column=0, sticky="nsew")
        btnID = tk.Button(navFrame, text='ID')
        btnID.pack()

        #as frames are added you need to add them below
        for F in (FrameA, FrameB, W2):
            page_name=F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=1, sticky="nsew")  #adjusted column
        
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

