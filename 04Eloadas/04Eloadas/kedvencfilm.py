def atvaltas(bPerc):
    ora=bPerc // 60
    perc=bPerc % 60
    return f"{ora} óra {perc} perc"

filmCime=input("Add meg a film címét!")
filmHossza=int(input("Hány perces a film?"))
print(f"A(z) {filmCime} című film {atvaltas(filmHossza)} hosszú.")