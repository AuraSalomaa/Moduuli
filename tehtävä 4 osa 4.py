import random
arvo = random.randint(1, 10)
while True:
    luku = int(input("Arvaa luku: "))
    if luku < arvo:
        print("Liian pieni arvaus..")
    elif luku > arvo:
        print("Liian suuri arvaus..")
    else:
        break
print("Oikein!")