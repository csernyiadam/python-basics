fajl = open("vito.txt", "r")
tesztSzam = int(fajl.readline().strip())
for i in range(tesztSzam):
    egyEset = fajl.readline().strip().split(" ")
    print(int(egyEset[len(egyEset)-1]) - int(egyEset[len(egyEset[1])]) )




fajl.close