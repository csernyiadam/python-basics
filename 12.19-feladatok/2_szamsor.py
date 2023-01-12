def kisebb(szamsor, parameter):
    db = 0
    for egySzam in szamsor:
        if (parameter > egySzam):
            db += 1
    return db

szamsor = [-14, 23, 1, -48, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77, 100]

print("Első feladat:")


print("Második feladat:")
utolsoIndex = -1  
for i in range(len(szamsor)):
    if (szamsor[i] % 7 == 0):
        utolsoIndex = i
print(utolsoIndex)

print("Harmadik feladat:")
for egySzam in szamsor== 0:
    print(egySzam /2)
print("Negyedik feladat:")
db = 0
print(len(szamsor))

print("Ötödik feladat:")
while ((not van) and (i < len(szamsor))):
    if (szamsor[i] < 0 and szamsor[i+1]>0):
        van = True
    i += 1
print(van, i)