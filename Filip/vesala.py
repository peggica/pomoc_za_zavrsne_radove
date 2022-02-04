import random 

Reci = ["robloks","olovka","vatra","pcela","knjiga","piton","robot","laptop","kaktus","kliker"]
rec = list(random.choice(Reci))

skrivena = []
for slovo in rec:
    skrivena.append("_")

broj_pokusaja = 15

def prikaz(rec):
    vrati = ""
    for slovo in rec:
        vrati += slovo
    return vrati
    
while rec != skrivena and broj_pokusaja > 0:
    print("vasa rec za pogadjanje je: " + prikaz(skrivena))
    ucitano = (input("upisi neko slovo: "))
    broj_pokusaja -= 1
    print("Preostali broj pokusaja: " + str(broj_pokusaja))
    for i in range(len(rec)):
        if ucitano.lower() == rec[i]:
            skrivena[i] = rec[i]

if rec == skrivena:
    print("Uspesno ste pogodili rec: " + prikaz(rec))
else:
    print("Nemate vise pokusaja!")
