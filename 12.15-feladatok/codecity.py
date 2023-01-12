import math
fajl = open("codecity.txt", "r")
for egySor in fajl:
    magassagok = egySor.strip().split(" ")
    ok = True
    for i in range(len(magassagok)-1):
        if (abs(int(magassagok[i])-int(magassagok[i+1]))>1:
            ok = False
fajl.close
