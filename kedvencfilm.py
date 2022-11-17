def filmek(filmbekeres):
        if(filmbekeres >= 60):
                return True
        else:
                return False
for i in range (3):
        textInput = input("Add meg egy film címét! ")
        filmLength = int(input("Hány perces a film?"))


        minute = filmLength%60
        hour = filmLength//60

        print(f"A(z) {textInput} című film {hour} óra {minute} perc hosszú.")
