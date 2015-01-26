from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get()) # pobiera wartosc feet
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0) #oblicza metry
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12") # ROZMIAR OKNA
mainframe.grid(column=0, row=0,  sticky=(N, W, E, S)) # umiejscowienie

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=10, textvariable=feet) # okienko tekstowe
feet_entry.grid(column=2, row=1, sticky=(W, E)) #ustawienie pola tekstowego feet_entry

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5) # for dla dziedziczonych z mainframe

feet_entry.focus() #kursos w polu tekstowym feet_entry
root.bind('<Return>', calculate) # nacisniecie enter potwierdza

root.mainloop()