#main.py

"""
depending on what page the user is on should dictate what NEXT and Previous do
if there is data already present, it shouild be presented.
if no data is present, things shoudl be blank.

"""
data_store = dict()


page_config = [
    {"type": "Label", "text": "Question 1:", "row": 0, "column": 0},
    {"type": "Entry", "row": 0, "column": 1, "key": "q1"},
    {"type": "Label", "text": "Question 2:", "row": 1, "column": 0},
    {"type": "Entry", "row": 1, "column": 1, "key": "q2"},
]   
page_config_1 = [
    {"type": "Label", "text": "First Name Middle Initial:", "row": 0, "column": 0},
    {"type": "Entry", "row": 0, "column": 1, "key": "_lname"},
    {"type": "Label", "text": "Last Name:", "row": 1, "column": 0},
    {"type": "Entry", "row": 1, "column": 1, "key": "_fname"},
] 

page_config_2 = [
    {"type": "Label", "text": "Wages:", "row": 0, "column": 0},
    {"type": "Entry", "row": 0, "column": 1, "key": "_w2_line1"},
    {"type": "Label", "text": "Tax Withheld:", "row": 1, "column": 0},
    {"type": "Entry", "row": 1, "column": 1, "key": "_w2_line2"},
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
        self.page3 = DynamicPage(self.container, page_config_1)

        # Place all pages in the same location
        self.page1.grid(row=0, column=0, sticky="nsew")
        self.page2.grid(row=0, column=0, sticky="nsew")
        self.page3.grid(row=0, column=0, sticky="nsew")

        # Raise the first page to show it
        self.page1.tkraise()
        self.current_page = self.page1
        # Add navigation buttons
        tk.Button(root, text="Next", command=self.show_page2).pack()
        tk.Button(root, text="page2", command=lambda: self.show_page(self.page2)).pack()
        tk.Button(root, text="page3", command=lambda: self.show_page(self.page3)).pack()

    def show_page(self, page_name):
        data = self.current_page.get_values()
        for k, v in data.items():
            data_store[k]=v    #this will over write data

        print(data)
        self.current_page = page_name
        page_name.tkraise()


    def show_page2(self):
        data =self.current_page.get_values()
        print(data)
        self.current_page = self.page2
        self.page2.tkraise()

root = tk.Tk()
app = App(root)
root.mainloop()   

print(data_store) #this works to print the entire dictionary but only when closing the app
