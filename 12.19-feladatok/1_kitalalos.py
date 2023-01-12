import random

print("Gondoltam egy számra 1 és 5 között")
bekertszam = int(input("Kérem, adjon meg egy egész számot: "))
gepiszam = random.randrange(1,6)

if bekertszam > gepiszam:
    print("Kisebbre gondoltam!")
elif bekertszam < gepiszam:
    print("Nagyobbra gondoltam!")
elif bekertszam == gepiszam:
    print("ELTALÁLTA!")
else:
    quit