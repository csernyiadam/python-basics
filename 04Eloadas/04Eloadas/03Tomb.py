import random

def Ertekeles(pontszam):
    if pontszam<=47:
        return 1
    if pontszam<=65:
        return 2
    if pontszam<=83:
        return 3
    if pontszam<=101:
        return 4
    return 5

Diakok=["Balázs Máté","Csernyi Ádám","Csitári Ádám","Csizmár Dániel","Fekete Dániel","Kovács Dániel","Kristály Adrián","Kutasi Erzsébet","Novák Domin","Oláh Márk","Papp János","Sándor Kristóf","Szabó Judit","Várdai Balázs","Zsóka Marcell"]
Pontszamok=[]
for i in range(len(Diakok)):
    Pontszamok.append(random.randrange(0,121))

for i in range(len(Diakok)):
    print(f"{Diakok[i]}: {Ertekeles(Pontszamok[i])}")
