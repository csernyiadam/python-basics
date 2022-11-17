def szavak():
    szo1 = input("Adj meg egy szót!")
    
    if szo1 == "":
        return "Nem adtál meg szót!"
    
    max = 0

    while len(szo1) > max :
        max = len(szo1)
        
        szo2 = input("Adj meg egy másik szót! ")

        if len(szo2) <= len(szo1):
            print (f"A hosszabb szó: {szo1}")
        else:
            print(f"A hosszabb szó: {szo2}")

szavak()