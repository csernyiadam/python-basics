print("Hello World!")

# Értékadó operátor

valtozo1=10
Valtozo1=20
valtozo2=45.678
valtozo3="Változó Három"
logikaiValtozo1=True

print(valtozo1)
print(Valtozo1) #Mérvadó a kis és nagy betű
print(valtozo2)
print(valtozo3)
print(logikaiValtozo1)


#Műveleti operátor ("+,-,*,/,%-maradék,//-egész")

valtozo4=3

print("Összeadás:")
eredmeny=valtozo1+valtozo4
print(eredmeny)

print("Kivonás:")
eredmeny2=valtozo1-valtozo4
print(eredmeny2)

print("Szorzás:")
eredmeny3=valtozo1*valtozo4
print(eredmeny3)

print("Osztás:")
eredmeny4=valtozo1/valtozo4
print(eredmeny4)

print("Egész:")
eredmeny5=valtozo1//valtozo4
print(eredmeny5)

print("Maradékos:")
eredmeny6=valtozo1%valtozo4
print(eredmeny6)

print("Szövegösszetűzés:")
valtozo5="-ő egy váltózó név"
eredmeny7=valtozo3+valtozo5
print(eredmeny7)

print("Adott szöveg sokszorosítás:")
eredmeny8=valtozo3*12
print(eredmeny8)

#2 a nyolcadikon  [Hatványozás]
print(2**8)

#Összehasonlító operátorok: "<,>, <=, >=, !=(nem egyenlő), =="
if(valtozo1<valtozo2):
    print("A 10 kisebb mint 20.")

if(valtozo1>valtozo4):
    print("Nagyobb!")

if(valtozo1<=valtozo2):
    print("A tíz kisebb vagy egyenlő mint húsz.")

if(valtozo1>=valtozo4):
    print("A három kisebb vagy egyenlő mint tíz.")
    
if(valtozo1!=valtozo2):
    print("A tíz nem húsz.")

#Logikai operátorok "and, or, not"
logikaivaltozo2=False
if((logikaiValtozo1 and logikaivaltozo2) and logikaiValtozo1):
    print("A két logikai változó értéke: [IGAZ]")
else:
    print("A két logikai változó értéke: [HAMIS]")

print(not logikaiValtozo1)
print(not logikaivaltozo2)
logikaiValtozo1=not logikaivaltozo2

szamlalo=0
if(logikaiValtozo1):
    szamlalo+=1
print(szamlalo)

valtozo6=22
valtozo7=1
if(valtozo6<valtozo7):
    print("Valtozo6 értéke kiseb mint a Valtozo7 értéke.")
elif(valtozo6>valtozo7):
    print("A valtozo6 értéke nagyobb mint a valtozo7 értéke.")
else:
    print("A két szám egyenlő.")

menuPont="A"
if(menuPont == "A"):
    print("'A' menupont lett kiválasztva.")
elif(menuPont == "B"):
    print("'B' menüpont lett kiválasztva.")
elif(menuPont == "C"):
    print("'C' menupont lett kiválasztva.")
else:
    print("Hibás menüpont lett kiválasztva")