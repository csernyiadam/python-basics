import math
fajl = open ("almafak.txt", "r")
testEsetekSzama = int(fajl.readline())


for i in range(testEsetekSzama):
    elsosor = fajl.readline().strip().split(" ")
    ladaTeherbiras = int(elsosor[0])
    ladakSzama = int(elsosor[1])
    AlmaFakSzama = int(elsosor[2])
    termesAlmafankent = fajl.readline().strip().split(" ")
    OsszLadaTeherbiras = ladaTeherbiras*ladakSzama
    OsszTermeles = 0
    for egyAlmafaTermese in termesAlmafankent:
        OsszTermeles += int(egyAlmafaTermese)
    if (OsszTermeles > OsszLadaTeherbiras):
        print("impossible")
    else:
        print(math.ceil(OsszTermeles / ladaTeherbiras))
fajl.close()