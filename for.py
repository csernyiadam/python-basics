futasokSzama = int(input("Hányszor futtassam a ciklust? "))
for i in range(futasokSzama):
    print(i)
for i in range(futasokSzama, 2, -1):
    print(i)
for i in range(futasokSzama, 2):
    print(i)
    

#2D tömb létrehozása [mátrix]
for i in range(20):
    print(str(i+1)+".",end="")
    for j in range(6):
        print("\t"+str(j+1), end="")
print()