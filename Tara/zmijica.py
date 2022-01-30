from tkinter import *
import random
from tkinter import messagebox

#kreiram prozor programa i platno
prozor = Tk()
platno = Canvas(prozor, width = 600, height = 600, bg = "green")
prozor.title("Zmijica igra")

#potrebne promenljive
zmijica_X = 300
zmijica_Y = 300
hrana_X1, hrana_Y1 = 100, 100
hrana_X2, hrana_Y2 = 120, 120
broj_poena = 0
pomeranje_X = 2
pomeranje_Y = 2

#dodavanje slike zmijice
zmijica_slika = PhotoImage(file = "snake.png")
zmijica = platno.create_image(zmijica_X, zmijica_Y, image = zmijica_slika)

#dodavanje hrane
hrana = platno.create_oval(100, 100, 120, 120, fill = "brown")

#dodavanje teksta o broju poena
poeni_tekst = platno.create_text(520, 30, text = "Poeni: 0", font = "Times 20")

def uvecaj_poene():
    global broj_poena
    broj_poena += 1
    platno.itemconfig(poeni_tekst, text = "Poeni: " + str(broj_poena))

def premesti_hranu():
    global hrana_X1, hrana_X2, hrana_Y1, hrana_Y2
    hrana_X1 = random.randrange(0, 580)
    hrana_Y1 = random.randrange(0, 580)
    hrana_X2 = hrana_X1 + 20
    hrana_Y2 = hrana_Y1 + 20
    platno.coords(hrana, hrana_X1, hrana_Y1, hrana_X2, hrana_Y2)
    
def pojedeno():
    global pomeranje_X, pomeranje_Y, hrana_X1, hrana_Y1, hrana_X2, hrana_Y2, zmijica_X, zmijica_Y
    #treba 4 uslova
    if (zmijica_Y - 36) < (hrana_Y2) and (hrana_Y2) < (zmijica_Y + 36) and (zmijica_X - 36) < (hrana_X2) and (hrana_X1) < (zmijica_X + 36):
        pomeranje_X *= 1.2
        pomeranje_Y *= 1.2
        uvecaj_poene()
        premesti_hranu()
        
def kraj_igre():
    global zmijica_X, zmijica_Y, broj_poena, poeni_tekst
    if (zmijica_Y > 564 or zmijica_Y < 36) or (zmijica_X > 550 or zmijica_X < 50):
        messagebox.showinfo("Kraj igre", "Poeni: " + str(broj_poena))
        zmijica_X = 300
        zmijica_Y = 300
        broj_poena = 0
        platno.coords(zmijica, zmijica_X, zmijica_Y)
        platno.itemconfig(poeni_tekst, text = "Poeni: " + str(broj_poena))
    
#pomeranje zmijice
def gornja_strelica(event):
    global zmijica_X, zmijica_Y, pomeranje_Y
    zmijica_Y -= pomeranje_Y
    platno.coords(zmijica, zmijica_X, zmijica_Y)
    kraj_igre()        
    pojedeno()
def donja_strelica(event):
    global zmijica_X, zmijica_Y, pomeranje_Y
    zmijica_Y += pomeranje_Y
    platno.coords(zmijica, zmijica_X, zmijica_Y)
    kraj_igre()     
    pojedeno()
def leva_strelica(event):
    global zmijica_X, zmijica_Y, pomeranje_X
    zmijica_X -= pomeranje_X
    kraj_igre()     
    pojedeno()
    platno.coords(zmijica, zmijica_X, zmijica_Y)
def desna_strelica(event):
    global zmijica_X, zmijica_Y, pomeranje_X
    zmijica_X += pomeranje_X
    platno.coords(zmijica, zmijica_X, zmijica_Y)
    kraj_igre()     
    pojedeno()

#povezivanje dogadjaja sa funkcijama
prozor.bind('<Up>', gornja_strelica)
prozor.bind('<Down>', donja_strelica)
prozor.bind('<Left>', leva_strelica)
prozor.bind('<Right>', desna_strelica)

platno.pack()
