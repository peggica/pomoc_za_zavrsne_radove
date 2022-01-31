from tkinter import *
from tkinter.colorchooser import askcolor

#kreiram prozor programa i platno
prozor = Tk()
platno = Canvas(prozor, width = 600, height = 600, bg = "white")
prozor.title("Igra crtanja")

boja = "black"
#dodato za odabir cetkice
platno.create_text(160, 30, text = "Odaberite veličinu četkice:", font = "Times 20")
platno.create_oval(350, 28, 356, 34, fill = boja, outline = boja)
platno.create_oval(370, 22, 386, 38, fill = boja, outline = boja)
platno.create_oval(400, 17, 426, 42, fill = boja, outline = boja)
kliknuta1 = True
kliknuta2 = False
kliknuta3 = False

def odabir_cetkice(event):
    global kliknuta1, kliknuta2, kliknuta3
    if((event.x > 350 and event.x < 356) and (event.y > 28 and event.y < 34)):
        kliknuta1 = True
        kliknuta2 = False
        kliknuta3 = False
    elif((event.x > 370 and event.x < 386) and (event.y > 22 and event.y < 38)):
        kliknuta2 = True
        kliknuta1 = False
        kliknuta3 = False
    elif((event.x > 400 and event.x < 426) and (event.y > 17 and event.y < 42)):
        kliknuta3 = True
        kliknuta1 = False
        kliknuta2 = False

def mis_pomeren(event):
    global kliknuta1, kliknuta2, kliknuta3
    #dodati uslovi
    
    if(event.y > 50):
        #ispod table za biranje
        if(kliknuta1):
            platno.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill = boja, outline = boja)
        if(kliknuta2):
            platno.create_oval(event.x - 8, event.y - 8, event.x + 8, event.y + 8, fill = boja, outline = boja)
        if(kliknuta3):
            platno.create_oval(event.x - 13, event.y - 13, event.x + 13, event.y + 13, fill = boja, outline = boja)

def odabir_boje(event):
    global boja
    boja = askcolor(title = "Odabir boje")[1]
    
#povezivanje dogadjaja sa funkcijama
prozor.bind("<Button-1>", odabir_cetkice)
prozor.bind("<B1-Motion>", mis_pomeren)
prozor.bind("<Button-3>", odabir_boje)

platno.pack()
