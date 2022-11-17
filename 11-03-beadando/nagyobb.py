elsoSzam = int (input("Adj meg egy számot! "))
masodikSzam = int (input("Adj meg egy másik számot! "))
if(elsoSzam > masodikSzam):
    print(f"A nagyobb érték {elsoSzam}")
elif(masodikSzam >elsoSzam):
    print(f"A nagyobb érték {masodikSzam}")
elif(masodikSzam == elsoSzam):
    print("A két szám egyenlő")

