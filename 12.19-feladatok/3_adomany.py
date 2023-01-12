from encodings import utf_8


fajl = open("segitok.txt", "r", encoding=utf_8)
for sor in fajl:
    mezok = sor.strip().split(";")
    egySegito = 
class Segito:
    def __init__(self, nev="", kezdes = 0, idotartam=0):
        self.nev = nev
        self.kezdes = kezdes
        self.idotartam = idotartam

    def Vegzes(self):
        return(self.kezdes+self.idotartam)
fajl.close