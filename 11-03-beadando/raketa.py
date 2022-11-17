visszaszamlalas = int(input("Hány orás visszaszámlálást tervezünk? "))
print(f"Visszaszámlálás: {visszaszamlalas}")

felfuggesztes = input("Fel kell függeszteni a visszaszámlálást? (i/n)")
if(felfuggesztes == "n"):
    print(f"Visszaszámlálás: {visszaszamlalas - 1}")
elif(felfuggesztes == "i"):
    print(f"Visszaszámlálás: {visszaszamlalas}")