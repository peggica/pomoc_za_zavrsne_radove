from tkinter import *

#kreiram prozor programa i platno
prozor = Tk()
platno = Canvas(prozor, width = 600, height = 600, bg = "green")
prozor.title("Zmijica igra")

#dodavanje slike zmijice
zmijica_slika = PhotoImage(file = "snake.png")
zmijica = platno.create_image(300, 300, image = zmijica_slika)

#dodavanje hrane
hrana = platno.create_oval(100, 100, 115, 115, fill = "light brown")

platno.pack()
