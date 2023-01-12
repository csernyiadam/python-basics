class Kenyer:
    def __init__(self, SutesiMod = "", GlutenMentes = False, Ar = 0, Szeletelt = False, Tomeg = 0, SzenhidratTartalom = 0, Tipus = ""):
        self.SutesiMod = SutesiMod
        self.GlutenMentes = GlutenMentes
        self.Ar = Ar
        self.Szeletelt = Szeletelt
        self.Tomeg = Tomeg
        self.SzenhidratTartalom = SzenhidratTartalom
        self.Tipus = Tipus
    def __str__(self):
        return(f"Tipus: {self.Tipus}\n Sütési mód: {self.SutesiMod}\n Gluténmentes: {self.GlutenMentes}\n Ár: {self.Ar}\n Szeletelt: {self.Szeletelt}\n Tömeg: {self.Tomeg} kg\n Szénhidrát tartalom: {self.SzenhidratTartalom}")
    
    def GlutenMentesE(self):
        if (self.GlutenMentes ):
            return "Igen"
        return
    def SzeleteltE(self):
        if(self.Szeletelt):
            return("Igen")
        return
    
kenyer1 = Kenyer("Kemencés", False, 1500, True, 50, )

kenyerek = []
fajl = open("kenyerkek.txt", "r", encoding="utf-8")
fajl.readline()
for sor in fajl:
    mezok = sor.strip().split(";")
    egyKenyer = Kenyer()
    egyKenyer.SutesiMod = mezok[0]
    if (mezok[1] == "igen"):
        egyKenyer.GlutenMentes = True
    egyKenyer.Ar = int(mezok[2])
    if(mezok [3] == "igen"):
        egyKenyer.Szeletelt = True
    egyKenyer.Tomeg = int(mezok[4])
    egyKenyer.SzenhidratTartalom = int(mezok[5])
    egyKenyer.Tipus = (mezok[6])
    kenyerek.append(egyKenyer)

fajl.close