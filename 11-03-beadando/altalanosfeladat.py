
for number in range(10, 51):
    if (number % 2 == 0):
        print(number)

negyzet = int(input("Adja meg a nézet oldalának hosszát: "))
print(f"A négyzet területe: {negyzet*negyzet}")
print(f"A négyzet kerülete: {negyzet+negyzet}")

teglalap1 = int(input("Adja meg a tégalalap egyik oldalának hosszát:"))
teglalap2 = int(input("Adja meg a téglalap másik oldalának hosszát: "))
print(f"A téglalap területe: {teglalap1 * teglalap2}")
print(f"A téglalap kerülete: {teglalap1 + teglalap2}")

szamok = [1,2,3,4,5,6,7,8,9,10]
if(szamok % 2 == 0):
  eredmeny = sum(szamok)
  print(eredmeny)