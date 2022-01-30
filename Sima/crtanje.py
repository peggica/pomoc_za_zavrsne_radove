from tkinter import *
from tkinter.colorchooser import askcolor

#kreiram prozor programa i platno
prozor = Tk()
platno = Canvas(prozor, width = 600, height = 600, bg = "white")
prozor.title("Igra crtanja")

boja = "black"

def mis_pomeren(event):
    print(boja)
    platno.create_oval(event.x - 1, event.y - 1, event.x + 1, event.y - 1, fill = boja, outline = boja)

def odabir_boje(event):
    global boja
    boja = askcolor(title = "Odabir boje")[1]
    
#povezivanje dogadjaja sa funkcijama
prozor.bind("<B1-Motion>", mis_pomeren)
prozor.bind("<Button-3>", odabir_boje)

platno.pack()
