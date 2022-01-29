from tkinter import *

#kreiranje prozora programa i platna
prozor = Tk()
platno = Canvas(prozor, width = 600, height = 400, bg = "darkblue")
prozor.title("Kviz igra")

tekst_broj_poena = platno.create_text(500, 50, text = "Broj poena: 0", font = "Times 20", fill = "white") 
tekst_pitanje = platno.create_text(300, 150, text = "Ovde ide neko pitanje?", font = "Times 30", fill = "white")

#iscrtavanje pravougaonika i teksta za dugmice
dugme1 = platno.create_rectangle(90, 220, 290, 280, fill = "lightblue", outline = "black")
tekst_dugme1 = platno.create_text(190, 250, text = "odgovor 1", font = "Times 20", fill = "white")
dugme2 = platno.create_rectangle(310, 220, 510, 280, fill = "lightblue", outline = "black")
tekst_dugme2 = platno.create_text(410, 250, text = "odgovor 2", font = "Times 20", fill = "white")
dugme3 = platno.create_rectangle(90, 300, 290, 360, fill = "lightblue", outline = "black")
tekst_dugme3 = platno.create_text(190, 330, text = "odgovor 3", font = "Times 20", fill = "white")
dugme4 = platno.create_rectangle(310, 300, 510, 360, fill = "lightblue", outline = "black")
tekst_dugme4 = platno.create_text(410, 330, text = "odgovor 4", font = "Times 20", fill = "white")

platno.pack()
