class AllatKereskedes:
    def __init__(self, Nev="", Faj="", Ar=0) -> None:
        self.Nev = Nev
        self.Faj = Faj
        self.Ar  = Ar
    def __str__(self) -> str:
        return (f"Név: {self.Nev}\nFajta: {self.Faj}\nÁr: {self.Ar} Ft.")
    def kiiras(self):
        print(f"Név: {self.Nev}\nFajta: {self.Faj}\nÁr: {self.Ar}Ft. ")

    def nagyker(self, vasarolniKivantDb):
        if (vasarolniKivantDb < 10):
            return self.Ar*vasarolniKivantDb
        elif(vasarolniKivantDb >= 10):
            return self.Ar*vasarolniKivantDb*.95
        else:
            return vasarolniKivantDb*self.Ar*.8

    
allat1 = AllatKereskedes("Bodri", "Kutya", 1000)
print(allat1)
allat1.kiiras()
allat1.nagyker(15)

tovabb = True
while (tovabb):
    egyAllat = AllatKereskedes()
    egyAllat.Nev = input("Kérem a dög nevít! ")
    if(egyAllat.Nev == ""):
        tovabb = False
    else:
        egyAllat.Faj = input("Kérem a dög faját! ")
        egyAllat.Ar = int(input("Mennyi a dög ára? "))