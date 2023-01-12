from encodings import utf_8


class idiotaVideo:
    def __init__(self,nev="", idoTartam=0.0, rang=0, agykarosodas=True, kategoria=""):
        self.nev = nev
        self.idoTartam = idoTartam
        self.rang = rang
        self.agykarosodas = agykarosodas
        self.kategoria = kategoria
    def agykar(self):
        if(self.agykarosodas):
            return("Igen")
        else:
            return("Nem")
            
    def __str__(self):
        return (f"Név: {self.nev}\tIdőtartam: {self.idoTartam}\tRang: {self.rang}\tAgykárosodás: {self.agykarosodas}\tKategória: {self.kategoria}")


idiotaVideo1 = idiotaVideo("SealSpin", 0.9, 1, True, "Lelki fájdalom elleni terápia")
idiotaVideo2 = idiotaVideo("Epic Sax Gandalf", 600, 1, True, "Felkavaró képsorok")
idiotaVideo3 = idiotaVideo()
idiotaVideo3.nev = input("Videó neve:")
idiotaVideo3.idoTartam = int(input("Időtartama:"))
idiotaVideo3.rang = int(input("Rang:"))
agykar = input("Agykárosodást okoz (igen/nem)")
if (agykar == "nem"):
    idiotaVideo3.agykarosodas = False
else:
    True

idiotaVideo3.kategoria = input("Kategória")

idiotaVideok = [idiotaVideo1, idiotaVideo2, idiotaVideo3]

index = 0
for i in range (1, len(idiotaVideok)):
    if (idiotaVideok[i].idoTartam>idiotaVideok[index].idoTartam):
        index = i
print(idiotaVideok[index].nev)
