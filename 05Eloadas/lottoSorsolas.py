import random
valaszthatoSzamokSzama = 90
hanyasLotto = 5

esely = 0
osztando = 1 
oszto = 1

for i in range(hanyasLotto):
    osztando *= valaszthatoSzamokSzama-i
    oszto *= (i+1)

esely = osztando/oszto  
print(f"Esély: 1:{esely:.0f}")


"""sajatSzamok = []
for i in range(5):
    bekertszam = int(input(f"Add meg a {i+1}. számot! "))
    sajatSzamok.append(bekertszam)"""
    
sajatSzamok = [5, 15, 30, 45, 60]
for i in range(10000):
    
    sorsoltSzamok = []
    while(len(sorsoltSzamok)<=hanyasLotto):
            sorsoltSzam = random.randrange(1, valaszthatoSzamokSzama+1)
    if(sorsoltSzam not in sorsoltSzamok):
            sorsoltSzamok.append(sorsoltSzam)

    talalatokSzama = 0
    for egySzam in sorsoltSzamok:
            if(egySzam in sajatSzamok):
                 talalatokSzama+=1
    print(f"Találatok száma: {talalatokSzama}")