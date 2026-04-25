#main.py





page_config = [
    {"type": "Label", "text": "Question 1:", "row": 0, "column": 0},
    {"type": "Entry", "row": 0, "column": 1, "key": "q1"},
    {"type": "Label", "text": "Question 2:", "row": 1, "column": 0},
    {"type": "Entry", "row": 1, "column": 1, "key": "q2"},
]   
page_config_1 = [
    {"type": "Label", "text": "First Name Middle Initial:", "row": 0, "column": 0},
    {"type": "Entry", "row": 0, "column": 1, "key": "q1"},
    {"type": "Label", "text": "Last Name:", "row": 1, "column": 0},
    {"type": "Entry", "row": 1, "column": 1, "key": "q2"},
] 

page_config_2 = [
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
    
    def get_values(self):
        """Returns a dictionary of current values: {key: value}"""
        return {k: v.get() for k, v in self.entries.items()}       



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
        self.current_page = self.page1
        # Add navigation buttons
        tk.Button(root, text="Next", command=self.show_page2).pack()

    def show_page2(self):
        data =self.current_page.get_values()
        print(data)
            
        self.page2.tkraise()

root = tk.Tk()
app = App(root)
root.mainloop()   


