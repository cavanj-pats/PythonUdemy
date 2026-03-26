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
        
        self.show_frame(FrameA)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update_data(self, text, target_frame):
        self.frames[target_frame].label.config(text=text)





if __name__ == "__main__":
    app = TestApp()
    app.mainloop()   



    """
    The `KeyError: <class 'FrameA.FrameA'>` occurs because you are trying to use the **class object** (`FrameA`) as a key in the `self.frames` dictionary, but the dictionary is actually keyed by the **class name as a string** (`"FrameA"`). 

The dictionary was populated like this:
```python
page_name = F.__name__ # This is a string, e.g., "FrameA"
self.frames[page_name] = frame # Key is the string "FrameA"
```

But you are trying to access it like this:
```python
self.frames[FrameA] # This looks for the class object as the key, which doesn't exist
```

To fix this, **pass the string name of the frame class** to `show_frame`, not the class itself. 

In your frame files, change:
```python
command=lambda: controller.show_frame(FrameA)
```
to
```python
command=lambda: controller.show_frame("FrameA")
```

Your `show_frame` method should then use the string to look up the frame:
```python
def show_frame(self, page_name): # page_name is a string
    frame = self.frames[page_name] # Look up by string key
    frame.tkraise()
```


    
    """