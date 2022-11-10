vezetekNev="Csernyi"
keresztNev="Ádám"
nev=vezetekNev+" "+keresztNev
print(nev)

a=vezetekNev
vezetekNev="Ismeretlen"
print(a)
print(vezetekNev)

#Logikai változóba tárolt
befogo1 = 3
befogo2 = 4
atfogo = 5

derekSzogu= befogo1**2 + befogo2**2 == atfogo**2
print(derekSzogu)

if(derekSzogu):
    print("A háromszög derékszögű.")
else:
    print("A háromszög nem derékszögű.")
menuPont = input("Add meg a menüpont betűjelét (A,B,C,D)").upper()
if(menuPont=="A"):
    print("Az 'A' menüpontot választottad.")
elif(menuPont=="B"):
    print("A 'B' menüpontot választottad.")
elif(menuPont=="C"):
    print("A 'C' menüpontot választottad.")
elif(menuPont=="D"):
    print("A 'D' menüpontot választottad.")
else:
    print("Hibás betűjelet adtál meg!")