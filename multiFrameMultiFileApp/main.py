# main.py
import tkinter as tk
from FrameA import FrameA
from FrameB import FrameB
from w2 import W2
from scheduleB import ScheduleB
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
        self.current_frame = None

        self.w2Data={}
        # Initialize frames from different files
        #need a navigation frame
        #ok to use grid just
        navFrame=tk.Frame(container, height=900, width=300, padx=50)
        navFrame.grid(row=0, column=0, sticky="nsew")
        self.btnID = tk.Button(navFrame, text='ID', command=self.calc_wages)
        self.btnID.pack()

        self.btnSchedB=tk.Button(navFrame,text='Schedule B', command=lambda: self.show_frame("ScheduleB"))
        self.btnSchedB.pack()
        
        lblIncome = tk.Label(navFrame)
        lblIncome.pack()

        
        
        #as frames are added you need to add them below
        for F in (FrameA, FrameB, W2, ScheduleB):
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
        self.current_frame = page_name

    def update_data(self, text, target_frame):
        #self.frames[target_frame].label.config(text=text)
        frame = self.frames[target_frame]
        frame.label.config(text=text)
        frame.tkraise()

    def calc_wages(self):
        #see if we can calculate total wages
        wages = 0
        for k, v in self.frames.items():
            
            if k[:2] == 'W2'  :
                #this is a W2
                #frame_data = self.frames[k].entry_data  # this works. this returns the entire dictionary
                #print(f"Frame Data: {frame_data}")
                wages += float(self.frames[k].varBox1.get())  #this does work!
        
        target = self.frames['FrameA']
        target.label.config(text=wages)
    
    
    

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




"""
    https://www.pythonguis.com/tutorials/input-validation-tkinter/

    https://www.google.com/search?q=python+tkinter+frame+with+many+entry+boxes+most+have+numeric+data+how+to+check+at+data+entry&ie=UTF-8

    https://www.google.com/search?q=python+tkinter+iterate+through+a+dictionary+to+populate+entry+box+initial+data.+dictionary+keys+represent+winfo.children%28%29&sxsrf=ANbL-n4mdlw7DbycG8KOe8HK3CJQARti5g%3A1775424860361

    https://www.google.com/search?q=python+tkinter+after+extracting+value+from+entry+box+how+do+i+reset+the+variable+from+a+function%3F&ie=UTF-8

    https://www.google.com/search?q=python+tkinter+convert+string+from+entry+box+to+float+using+get.&ie=UTF-8


    https://www.google.com/search?q=python+tkinter+loop+through+all+entry+widgets+and+save+their+data+to+a+dictionary+with+entry+widget+name+as+the+key&ie=UTF-8


"""

"""
page_config = [
    {"type": "Label", "text": "Question 1:", "row": 0, "column": 0},
    {"type": "Entry", "row": 0, "column": 1, "key": "q1"},
    {"type": "Label", "text": "Question 2:", "row": 1, "column": 0},
    {"type": "Entry", "row": 1, "column": 1, "key": "q2"},
]   



import tkinter as tk

class DynamicPage(tk.Frame):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.entries = {}  # Store Entry widgets to retrieve values later
        for widget_info in config:
            widget_type = widget_info["type"]
            row = widget_info["row"]
            column = widget_info["column"]
            # Create the widget based on the 'type' key
            if widget_type == "Label":
                widget = tk.Label(self, text=widget_info["text"])
            elif widget_type == "Entry":
                widget = tk.Entry(self)
                # Optionally store the entry with a key for later access
                if "key" in widget_info:
                    self.entries[widget_info["key"]] = widget
            # Add the widget to the grid
            widget.grid(row=row, column=column, padx=5, pady=5)   


class App:
    def __init__(self, root):
        self.container = tk.Frame(root)
        self.container.pack()

        # Create different pages using the same class but different configs
        self.page1 = DynamicPage(self.container, page_config_1)
        self.page2 = DynamicPage(self.container, page_config_2)

        # Place all pages in the same location
        self.page1.grid(row=0, column=0, sticky="nsew")
        self.page2.grid(row=0, column=0, sticky="nsew")

        # Raise the first page to show it
        self.page1.tkraise()

        # Add navigation buttons
        tk.Button(root, text="Next", command=self.show_page2).pack()

    def show_page2(self):
        self.page2.tkraise()

root = tk.Tk()
app = App(root)
root.mainloop()   




this is a method for keeping multiple instances 
of the same class separate for data purposes.

class DynamicPage(tk.Frame):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.entries = {}  # This dictionary is unique to each instance
        for widget_info in config:
            if widget_info["type"] == "Entry":
                entry = tk.Entry(self)
                self.entries[widget_info["key"]] = entry  # Store with a unique key   
"""