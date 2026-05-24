import tkinter as tk
#Fabio Musanni you tube video
class MyApp(tk.Frame):

    def __init__(self, root):
        
        self.current_page_index = 0
        self.pages=[self.page1, self.page2, self.page3, self.page4]
        
        self.color1='#222448'
        self.color2='#54527E'
        self.color3 = 'WHITE'

        super().__init__(
            root,
            bg=self.color1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.rowconfigure(0,weight=1)

        self.load_main_widgets()


    def load_main_widgets(self):
        self.create_page_container()
        self.create_pager()
        self.pages[self.current_page_index]()  #include parentheses to call the function

    #i think he deletes this later
    #def clear_frame(self, frame):
    #    for child in frame.winfo_children():
    #        child.destroy()

    def create_page_container(self):
        
        self.page_container = tk.Frame(
            self.main_frame,
            background=self.color1
        )

        self.page_container.columnconfigure(0, weight=1)
        self.page_container.rowconfigure(0, weight=0)
        self.page_container.rowconfigure(1, weight=1)

        self.page_container.grid(column=0, row=0, sticky=tk.NSEW)
        # ************** this block of code was in each page function now it is here ****
        self.title = tk.Label(
            self.page_container,
            foreground=self.color3,
            background=self.color1,
            height=2,
            font=('Arial', 26, 'bold')
        )

        self.title.grid(column=0, row=0)

        text = ('This is the text that needs to be used.'
                'python can concatenate these multiple lines'
                'into the text that we wish to be visible')
        
        self.content = tk.Label(
            self.page_container,
            background=self.color2,
            foreground=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial', 16),
            wraplength=600
        )

        self.content.grid(column=0, row=1, sticky=tk.NSEW)
        #   **************   End of the block of  code  ********

    def create_pager(self):
        
        self.pager=tk.Frame(
            self.main_frame,
            background=self.color1,
            height=125,
            width=400
        )

        self.pager.columnconfigure(1, weight=1)
        self.pager.rowconfigure(0, weight=1)
        self.pager.grid(column=0, row=1, sticky=tk.NS)
        self.pager.grid_propagate(False)

        def change_page(button):
            #self.clear_frame(self.page_container)  #this is deleted now

            match button:
                case 'Previous':
                    self.current_page_index -= 1
                    self.pages[self.current_page_index]()
                case 'Next':
                    self.current_page_index += 1
                    self.pages[self.current_page_index]()
            
            self.page_number['text']=f'{self.current_page_index + 1}/{len(self.pages)}'

            if self.current_page_index == 0:
                prev_button.config(state = tk.DISABLED)
            elif self.current_page_index == len(self.pages)-1:
                next_button.config(state = tk.DISABLED)
            else:
                prev_button.config(state = tk.ACTIVE)
                next_button.config(state = tk.ACTIVE)

        prev_button = tk.Button(
            self.pager,
            background=self.color2,
            foreground=self.color3,
            activebackground=self.color2,
            activeforeground=self.color3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial', 18),
            cursor='hand1',
            text='Previous',
            state=tk.DISABLED,
            command= lambda button='Previous': change_page(button)
        )

        prev_button.grid(column=0, row=0)

        self.page_number = tk.Label(
            self.pager,
            background=self.color1,
            foreground=self.color3,
            font=('Arial, 18'),
            text=f'{self.current_page_index + 1}/{len(self.pages)}'
        )

        self.page_number.grid(column=1, row=0)

        next_button = tk.Button(
            self.pager,
            background=self.color2,
            foreground=self.color3,
            activebackground=self.color2,
            activeforeground=self.color3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial', 18),
            cursor='hand1',
            text='Next',
            command = lambda button='Next': change_page(button)
        )

        next_button.grid(column=2, row=0)

    def page1(self):

        text = ('This is the text that needs to be used.'
                'python can concatenate these multiple lines'
                'into the text that we wish to be visible')
        
        self.title.config(text='Page 1')
        self.content.config(text=text)


    def page2(self):

        text = ('This is Page 2 of the text that needs to be used.'
                'python can concatenate these multiple lines'
                'into the text that we wish to be visible')
        
        self.title.config(text='Page 2')
        self.content.config(text=text)
        

    def page3(self):

        text = ('This is Page 3 the text that needs to be used.'
                'python can concatenate these multiple lines'
                'into the text that we wish to be visible')
        
        self.title.config(text='Page 3')
        self.content.config(text=text)
       


    def page4(self):

        text = ('This is Page 4 of the text that needs to be used.'
                'python can concatenate these multiple lines'
                'into the text that we wish to be visible')
        
        self.title.config(text='Page 4')
        self.content.config(text=text)
     

root = tk.Tk()
root.title('Multi Page App')
root.geometry('700x500')
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()


