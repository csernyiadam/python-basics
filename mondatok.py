import random
def nevelo(szo):
    maganhangzok = 'aáeéiíoóöőuú'
    if szo[0].lower() in maganhangzok:
        return "Az"
    else:
        return "A"
        
        
def jelzo():
    return random.choice(['piros', 'nagy', 'könnyed'])

print("Add meg a 3 főnevet! ")
for i in range(3):
    
   fonev = input(f"(i+1). Főnév: ")
   print(f"{nevelo(fonev)} {fonev} {jelzo()}.")
    
