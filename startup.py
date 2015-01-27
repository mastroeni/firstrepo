from tkinter import *
from tkinter import ttk



class Application:
#def Facebook(*args)
#def Twitter(*args)
#def Instagram(*args)
#def Youtube(*args)

    def __init__(self, parent):
        self.parent = parent
        self.combo()
        self.label()
        self.button()

    def combo(self):
        self.chSocial = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.chSocial, state='readonly')
        self.box['values'] = ('Facebook', 'Twitter', 'Instagram', 'Youtube')
        self.box.current(0)
        self.box.grid(column=0, row=2, rowspan=3, padx=20)

    def label(self):
        self.choose = ttk.Label(self.parent, text="Choose social media")
        self.choose.grid(column=0, row=1, pady=5)
        self.result = ttk.Label(self.parent, text="Your result")
        #self.result.grid(column=4,row=1, padx=50)
        # wyświetlanie wyników wyszukiwania

    def button(self):
        self.buttonek = ttk.Button(self.parent, text='Search')
        self.buttonek.grid(column=0, row=5, pady=80)

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.geometry('400x300')
    root.title("Start up")
    root.mainloop()
