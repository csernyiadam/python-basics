def loginAccept (inputUsername, inputPassword):
    username = "user1"
    password = "password1"
    if(inputUsername == username and inputPassword == password):
        return True
    else:
        return False
loginAccepted = False

while(not loginAccepted):
    userin = input("Adja meg a felhasználónevét! ")
    passwdin = input("Adja meg a jelszavát! ")
    loginAccepted = loginAccepted(userin, passwdin)
    if(not loginAccepted):
        print("Belépés megtagadva! ")
    print("Belépés engedélyezve.")