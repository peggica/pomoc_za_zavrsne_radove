from tkinter import *
import time
import random
from tkinter import messagebox

prozor = Tk()
platno = Canvas(prozor, width = 600, height = 600, bg = "lemon chiffon")
prozor.title("Zmija")

pojeni = 0
pojeni_tekst = platno.create_text(90, 20, text = "Broj pojena: 0", font = "Times 20")

krugX1 = 100
krugY1 = 100
krugX2 = 125
krugY2 = 125
krug = platno.create_oval(krugX1,krugY1,krugX2,krugY2, fill = "gold")

ZX = 300
ZY = 300
slika_zmije = PhotoImage(file = "zmija.png")
zmija = platno.create_image(ZX, ZY, image = slika_zmije)

crtanje = True
brzina = 3

def izlazak():
  global crtanje
  crtanje = False
  prozor.destroy()

def taster_pritisnut(e):
  global ZX, ZY
  while crtanje:
    if e.keysym == "Up":
      if(ZY-30 > 0):
        ZY -= brzina
        platno.coords(zmija, ZX, ZY)
      else:
        kraj()
        break
        
    elif e.keysym == "Down":
      if(ZY+30 < 600):
        ZY += brzina
        platno.coords(zmija, ZX, ZY)
      else:
        kraj()
        break
        
    elif e.keysym == "Left":
      if(ZX-23 > 0):
        ZX -= brzina
        platno.coords(zmija, ZX, ZY)
      else:
        kraj()
        break
        
    elif e.keysym == "Right":
      if(ZX+23 < 600):
        ZX += brzina
        platno.coords(zmija, ZX, ZY)
      else:
        kraj()

    sudar()
    prozor.update()
    time.sleep(0.016)
  
prozor.bind("<KeyPress>", taster_pritisnut)
prozor.protocol("WM_DELETE_WINDOW", izlazak)

def sudar():
  global krugX1, krugY1, krugX2, krugY2, krug, pojeni, brzina
  if krugX2>ZX-23 and krugX1< ZX+23 and krugY2>ZY-30 and krugY1<ZY+30:
    krugX1 = random.randrange(25, 550)
    krugY1 = random.randrange(25, 550)
    krugX2 = krugX1 + 25
    krugY2 = krugY1 + 25
    platno.coords(krug, krugX1, krugY1, krugX2, krugY2)
    pojeni += 1
    brzina += 0.05
    platno.itemconfig(pojeni_tekst, text = "Broj poena: " + str(pojeni))

def kraj():
  global crtanje
  if(crtanje):
    platno.delete("all")
    messagebox.showinfo("Kraj igre", "Ukupan broj poena: " + str(pojeni))
    crtanje = False
  
platno.pack()
