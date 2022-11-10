from itertools import count


bekertMondat = input("Irj be egy mondatot.")
eBetukSzama = 0
for betu in bekertMondat:
    if(betu == "e"):
        eBetukSzama += 1
print(f"A megadott mondatban {eBetukSzama} db 'e' betű található.")