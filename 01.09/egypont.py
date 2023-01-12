'''szam1 = int(input("Adjon meg egy számot! "))
szam2 = int(input("Adjon meg egy másik számot! "))

if(szam1 > szam2):
    print(f"{szam1} volt a nagyobb.")
elif(szam1 < szam2):
    print(f"{szam2} volt a nagyobb.")
else:
    print("A két szám egyenlő.")
'''


szam1 = int(input("Adjon meg egy számot! "))
szam2 = int(input("Adjon meg egy másik számot! "))

if(szam1 % 7 == 0):
    print(f"{szam1} osztható 7-tel.")
elif(szam2 % 7 == 0):
    print(f"{szam2} osztható 7-tel.")
elif((szam1 % 7 == 0) and (szam2 % 7 == 0)):
    print(f"Mind a két szám osztható 7-tel.")
else:
    print("A két szám nem osztható 7-tel.")
