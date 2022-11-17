username = "bori99"
password = "Szivecske<3"
usernameInput = ""
while(usernameInput != username):

    usernameInput = input("Adja meg a felhasználónevét! ")
    passwordInput = input("Adja meg a jelszavát! ")
    if(usernameInput == username and passwordInput == password):
        print("Belépés engedélyezve!")
        usernameInput = ""
    else:
        print("Belépés megtagadva!")
        usernameInput = ""
