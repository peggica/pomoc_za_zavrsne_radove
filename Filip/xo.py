from tkinter import *
import random

#kreiram prozor programa i platno
prozor = Tk()
platno = Canvas(prozor, width = 600, height = 600, bg = "sandy brown")
prozor.title("XO igra")

#iscrtavanje 4 linije za polja
platno.create_line(195, 0, 195, 600, fill = "white", width = 10)
platno.create_line(395, 0, 395, 600, fill = "white", width = 10)
platno.create_line(0, 195, 600, 195, fill = "white", width = 10)
platno.create_line(0, 395, 600, 395, fill = "white", width = 10)

racunar_igra = False

#random biranje X ili O za nas i za racunar za pocetak igre
listaXO = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
mi = random.choice(listaXO)
#moglo je bolje ali neka ga ovako
racunar = ""
if mi == "X":
    racunar = "O"
else:
    racunar = "X"
    racunar_igra = True

def kliknuto(event):
    print(event.x, event.y)
    #ovo treba da nacrta X ili Y na tom mestu

def binding():
    #povezivanje dogadjaja sa funkcijom
    prozor.bind("<Button-1>", kliknuto)

def glavna_petlja():
    #potrebno cekanje na klik
    global racunar_igra
    while True:
        if racunar == "X":
            if(racunar_igra == True):
                pozicija_X = random.randrange(1, 9)
                print(pozicija_X)
                racunar_igra = False
            else:
                binding()
                #racunar_igra = True
            
        elif racunar == "O":
            binding()
            #racunar_igra = True
            if(racunar_igra == True):
                pozicija_X = random.randrange(1, 9)
                print(pozicija_X)
                racunar_igra = False

platno.pack()
glavna_petlja()
