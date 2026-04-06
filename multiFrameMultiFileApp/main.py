# main.py
import tkinter as tk
from FrameA import FrameA
from FrameB import FrameB
from w2 import W2
"""
    There will be forms (frames) with only one instance.  
    in fact i would believe most will be one instance.
    W2 forms can have more than one instance.
    'main' aka controller should manage this....
    I don't like client classes needing to know Instance ID
"""

class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global container 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        self.frames = {}
        self.w2Data={}
        # Initialize frames from different files
        #need a navigation frame
        #ok to use grid just
        navFrame=tk.Frame(container, height=900, width=300, padx=50)
        navFrame.grid(row=0, column=0, sticky="nsew")
        btnID = tk.Button(navFrame, text='ID')
        btnID.pack()
        
        lblIncome = tk.Label(navFrame)
        lblIncome.pack()

        
        
        #as frames are added you need to add them below
        for F in (FrameA, FrameB, W2):
            page_name=F.__name__
            #instance_id = f"{F.__name__}_{len(self.frames)}"
            #self.frame_instance_id += 1
            #instance_id = f"{F.__name__}_{self.frame_instance_id}"
            
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=1, sticky="nsew")  #adjusted column

        

        self.show_frame("FrameA")   #this should be the first item in the dictionary
                                     #if this changes it'll need to be changed.
        """
        self.create_new_instance("FrameA")
        """
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update_data(self, text, target_frame):
        #self.frames[target_frame].label.config(text=text)
        frame = self.frames[target_frame]
        frame.label.config(text=text)
        frame.tkraise()

    
    
    
    
    

    def create_new_instance(self, frame_class):
        # 1. Generate a unique key for the dictionary
        instance_id = f"{frame_class.__name__}_{len(self.frames)}"
        
        # 2. Create the new frame instance
        # Pass 'self' as the controller so it can call show_frame later
        new_frame = frame_class(container, self)

        # 3. Add to your existing dictionary
        self.frames[instance_id] = new_frame

        # 4. Position it (usually in the same grid slot as others)
        new_frame.grid(row=0, column=1, sticky="nsew")

        # 5. Show the newly created frame
        self.show_frame(instance_id)





if __name__ == "__main__":
    app = TestApp()
    app.mainloop()   

