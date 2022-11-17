from math import sqrt
class record:
                #formális paraméter lista
    def __init__(self, ora=0, perc=0, masodperc=0, X=0, Y=0):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
        self.X = X
        self.Y = Y

def elteltIdoSzamitasa(kezdoOra, kezdoPerc, kezdoMasodperc, zaroOra, zaroPerc, zaroMasodperc):
    kezdoIdo = kezdoOra*3600+kezdoPerc*60+kezdoMasodperc
    zaroIdo = zaroOra*3600+zaroPerc*60+zaroMasodperc
    return zaroIdo - kezdoIdo
    
    
print("1. feladat")
jeladatok = [] #listát definiálhatunk
fajl = open("jel.txt", "r")
for sor in fajl:
    mezok = sor.strip().split(' ')
    egyRecord = record() #példányosítottunk egy record típusú objektumot egyRecord néven
    egyRecord.ora = int(mezok[0])
    egyRecord.perc = int(mezok[1])
    egyRecord.masodperc = int(mezok[2])
    egyRecord.X = int(mezok[3])
    egyRecord.Y = int(mezok[4])
    
    jeladatok.append(egyRecord)
    
fajl.close()

print("2. feladat")
jelSorszama = int(input("Adja meg a jel sorszámát! "))
print(f"x={jeladatok[jelSorszama-1].X} y={jeladatok[jelSorszama-1].Y}") #index szerinti pozícióját megadva hivatkozok az adatra

print("4. feladat")
utolso = len(jeladatok)-1
elteltIdo = elteltIdoSzamitasa(jeladatok [0].ora, jeladatok [0].perc, jeladatok [0].masodperc, jeladatok [utolso].ora, jeladatok [utolso].perc, jeladatok [utolso].masodperc)

oraKi = elteltIdo // 3600
maradekIdo = elteltIdo % 3600
percKi = maradekIdo // 60
masodpercKi = maradekIdo % 60
print(f"Időtartam: {oraKi}:{percKi}:{masodpercKi} ")

print("5. feladat")
minX = jeladatok[0].X
minY = jeladatok[0].Y
maxY = jeladatok[0].Y
maxX = jeladatok[0].X

for i in range(1, len(jeladatok)):
    if jeladatok[i].X < minX:
        minX = jeladatok[i].X
    if jeladatok[i].X > maxX:
        maxX = jeladatok[i].X
    if jeladatok[i].Y < minY:
        minX = jeladatok[i].Y
    if jeladatok[i].Y > maxY:
        maxX = jeladatok[i].Y
        
print(f"Bal alsó: {minX}{minY}, jobb felső: {maxX}{maxY}")

print("6. feladat")
szum = 0
for i in range(len(jeladatok)-1):
    tavolsag = sqrt((jeladatok[i].X-jeladatok[i+1].X)**2+(jeladatok[i].Y-jeladatok[i+1].Y)**2)
    szum += tavolsag
print(f"Elmozdulás: {round(szum, 3)} egység")

print("7. feladat")
for i in range(len(jeladatok)-1):
    kulonbseg = elteltIdoSzamitasa(jeladatok[i].ora, jeladatok[i].perc, jeladatok[i].masodperc, jeladatok[i+1].ora, jeladatok[i+1].perc, jeladatok[i+1].masodperc)
    if(kulonbseg > 300):
        print(kulonbseg, jeladatok[i+1].ora, jeladatok[i+1].perc, jeladatok[i+1].masodperc)
        
fajl = open ("kimaradt.txt", "w") #file létrehozasa

fajl.close()