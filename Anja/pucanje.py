from tkinter import *

#kreiram prozor programa i platno
prozor = Tk()
platno = Canvas(prozor, width = 800, height = 500, bg = "rosy brown")
prozor.title("Pucanje igra")

#dodavanje slike pistolja
pistolj_slika = PhotoImage(file = 'gun.png')
pistolj = platno.create_image(50, 250, image = pistolj_slika)

#dodavanje slike mete
meta_slika = PhotoImage(file = 'target.png')
meta = platno.create_image(700, 250, image = meta_slika)

platno.pack()
