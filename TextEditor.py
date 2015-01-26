
#!/usr/bin/python
from tkinter import *


def closeWindow(zdarznie):
    root.quit() # przerywa tryb nasluchiwania zdarzen
    root.destroy() # zwalnia zasoby

root = Tk()
# Code to add widgets will go here...
root.geometry('500x300') # rozmiar okna
root.title("This is a title") # tytul

labelek = Label(root, text="Mos", font=("Arial",24,"italic"),foreground="yellow",background="blue") #ustawienia okna, zolte litery na niebieskim tle
labelek.pack(expand=YES, fill=BOTH) # fill(poziomo,pionowo, na dwie strony), expand (rozszerza sie wraz z powiekszeniem okna)

buttonek = Button(root, text="Close window", background="red", command=closeWindow) #(root=Tk(), tekst na oknie, tlo przycisku, funkcja wywolana)
buttonek.pack() # umieszcza przycisk (side = LEFT,BOTTOM, etc, fill-rozszerza)
buttonek.bind("<Enter>", closeWindow) # <Enter> - najechanie myszka, <Button> nacisniecie, closeWindow - funkcja


root.mainloop() # oczekuje na akcje