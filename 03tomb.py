import random
def ertekeles (pontok):
    if pontok <= 47:
        return 1
    elif pontok <= 65:
        return 2
    elif pontok <= 83:
        return 3
    elif pontok <= 101:
        return 4
    return 5

students = ["Zsóka Marcell", "Balázs Máté", "Fekete Dániel", "Kutasi Erzsébet", "Szabó Judit", "Papp János", "Novák Dominik", "Várdai Balázs",  "Márk Oláh", "Kovács Dániel", "Csizmár Dániel", "Csitári Ádám", "Csernyi Ádám", "Kristály Adrián", "Illés Kristóf"]
points = []

for  i in range (len(students)):
    points.append(random.randrange(0,121))

for i in range(len(students)):
    print(f"{students[i]}: {ertekeles(pontok=[i])} ")