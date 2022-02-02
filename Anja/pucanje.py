from tkinter import *
import time
import random
from tkinter import messagebox

prozor = Tk()
platno = Canvas(prozor,width = 800, height = 800, bg = "white")
prozor.title("Shooter")

platno.pack()

poeni = 0
crtanje = True
poeni_tekst = platno.create_text(700, 50, text = "Broj poena: 0", font = "Times 20", fill = "black")

gun_X = 100
gun_Y = 400
gun_slika = PhotoImage(file = "gun.png" )
gun = platno.create_image(gun_X, gun_Y, image = gun_slika)

target_X = 700
target_Y = random.randrange(50,750)
target_slika = PhotoImage(file = "target.png")
target = platno.create_image(target_X, target_Y, image = target_slika)

def uvecaj_poene():
    global poeni
    poeni += 1
    platno.itemconfig(poeni_tekst, text="Poeni: "+str(poeni))
    
def pomeraj(e):
    if(e.y>50 and e.y<750):
        platno.coords(gun, gun_X, e.y)

def onClose():
    global crtanje
    crtanje = False
    prozor.destroy()
    
def pucaj(e):
    brzina = 0
    global target_X, target_Y, target, crtanje
    mx1=200
    mx2=230
    my1=e.y-50
    my2=e.y-30
    metak = platno.create_oval(mx1, my1, mx2, my2, fill="yellow", outline="orange", width=4)
    while(True):
        if(crtanje):
            mx1 += 30
            mx2 += 30
            platno.coords(metak, mx1, my1, mx2, my2)
            prozor.update()
            time.sleep(0.016)
            if(mx2>target_X-50 and mx2<target_X+50 and my2<target_Y+50 and my1>target_Y-50):
                uvecaj_poene()
                target_Y = random.randrange(50,750)
                brzina += 3
            if(target_X+50>gun_X+200):
                target_X -= brzina
                platno.coords(target, target_X, target_Y)
                
            else:
                if(crtanje):
                    messagebox.showinfo("Kraj igre", "Ukupan broj poena: "+ str (poeni))
                    platno.delete(target)
                crtanje = False
        else:
            
            break

prozor.bind("<Button-1>", pucaj)
prozor.bind("<Motion>", pomeraj)
prozor.protocol("WM_DELETE_WINDOW", onClose)