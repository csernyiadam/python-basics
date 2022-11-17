import random

Helyszin = ["Brazíliában","Irakban","a muszkás-oldal dűlőben","az Avason","a Blaha Lújza téren","Alabamában","az asztalon","a mosdóban","a hálószobában","a pincében","a kenyérszeletelőn","a hűtőszekrényben"]
Idopont = ["tegnap","holnap","másnap","a jövőben","április 20-án","szeptember 11-én","amikor piros hó esett","kiskedden","a születése napján","június 9-én","fizunapon","segélynapon"]
Cselekves = ["csókolózotak","lefeküdtek","felálltak","beleültek egy rajzszögbe","leitták magukat","hegesztettek","szeretkeztek","kúpoltak","elmentek","veszekedtek","jól megkapták a magukét","etyepetyéltek","fifázgattak","paníroztak","főztek","összekaptak mint a kutyák","unga-bungáztak"]
KiKivel = ["Balázs Máté","Csernyi Ádám","Csitári Ádám","Csizmár Dániel","Fekete Dániel","Kovács Dániel","Kristály Adrián","Kutasi Erzsébet","Novák Domin","Oláh Márk","Papp János","Sándor Kristóf","Szabó Judit","Várdai Balázs","Zsóka Marcell"]
emberekSzama = (KiKivel)
ki = random.randrange(emberekSzama)
kivel = ki

for i in range(5):
    kivel = random.choice(emberekSzama)
    print(ki,kivel)
    hol = random.choice(Helyszin)
    mikor = random.choice(Idopont)
    mit = random.choice(Cselekves)
    print(f"{KiKivel[ki]} és {KiKivel[kivel]} {Helyszin[hol]} {Idopont[mikor]} {Cselekves[mit]}.")