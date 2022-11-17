currentTime = int(input("Hány óra van most? "))
openTime = [8,9,10,11,12,13,14,15,16]
closingTime = max(openTime)
if(currentTime in openTime):
    print("A bolt nyitva van")
    print(f"Ennyi órád van még odaérni: {closingTime - currentTime}")
elif(currentTime not in openTime):
    print("A bolt zárva van")

