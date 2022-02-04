from tkinter import *
from tkinter import messagebox

prozor = Tk()
platno = Canvas(prozor, width = 1300, height = 700, bg="dark blue")
labelKviz = Label(prozor, text="Kviz", font = ("Arial", 50), bg = "dark blue")
labelKviz.place(x=600, y=50)
prozor.title("Kviz")
labelIme = Label(prozor, text="Unesite ime =", font = ("Arial", 30), bg = "darkblue")
labelIme.place(x=300, y=250)
entryIme = Entry(prozor, font = ("Arial", 30))
entryIme.place(x=550, y=250)

ime = entryIme.get()

poeni_text = platno.create_text(150, 50, text = "", font = "Times 20", fill = "white")
poeni = 0

pitanje = StringVar()
pitanje.set("Koje godine je napravljen prvi elektronski racunar?")

button1 = Button(prozor, text = "a)1940", font=("Arial",30), bg="lightblue", command = lambda klik=1: izabran_odgovor(klik))
button2 = Button(prozor, text = "b)1941", font=("Arial",30), bg="lightblue", command = lambda klik=2: izabran_odgovor(klik))
button3 = Button(prozor, text = "c)1943", font=("Arial",30), bg="lightblue", command = lambda klik=3: izabran_odgovor(klik))
button4 = Button(prozor, text = "d)1947", font=("Arial",30), bg="lightblue", command = lambda klik=4: izabran_odgovor(klik))
   
pitanje1 = True
pitanje2 = False
pitanje3 = False

def izabran_odgovor(klik):
   global poeni, pitanje1, pitanje2, pitanje, pitanje3
   if pitanje1:
      if klik == 3:
         poeni += 1
         platno.itemconfig(poeni_text, text = "Broj poena = " + str(poeni))
         platno.update()
      pitanje.set("Kako se zvao prvi elektronski racunar?")
      button1.config(text = "a) Eniac")
      button2.config(text = "b) Enigma")
      button3.config(text = "c) Envat")
      button4.config(text = "d) Enfa")
      pitanje1 = False
      pitanje2 = True
   elif pitanje2:
      if klik == 1:
         poeni += 1
         platno.itemconfig(poeni_text, text = "Broj poena = " + str(poeni))
         platno.update()
      pitanje.set("Najpristiznija nagrada iz informatike nosi ime po kom naucniku?")
      button1.config(text = "a) Ada Lavlejs")
      button2.config(text = "b) Dzon Nojman")
      button3.config(text = "c) Alan Tjuring")
      button4.config(text = "d) Albert Ajnstajn")
      pitanje2 = False
      pitanje3 = True
   elif pitanje3:
      if klik == 3:
         poeni += 1
         platno.itemconfig(poeni_text, text = "Broj poena = " + str(poeni))
         platno.update()
      pitanje3 = False
      messagebox.showinfo("Kraj Igre", "Broj poena za: " + ime + " je: " + str(poeni))


def submit():
   global ime
   ime = entryIme.get()
   labelKviz.destroy()
   labelIme.destroy()
   entryIme.destroy()
   button_submit.destroy()
   pitanje1 = Label(prozor, textvariable = pitanje, font = ("Arial",30), bg = "dark blue")
   pitanje1.place(x=100,y=150)
   platno.itemconfig(poeni_text, text = "Broj poena = " + str(poeni))
   button1.place(x=400,y=300)
   button2.place(x=800,y=300)
   button3.place(x=400,y=400)
   button4.place(x=800,y=400)
   
button_submit = Button(prozor, text="Nastavi", font = ("Arial", 30), command = submit)
button_submit.place(x=600,y=400)
platno.pack()
