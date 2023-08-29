import random
arvo = random.randint(1, 10)
while True:
    luku = int(input("Arvaa luku: "))
    if arvo != luku:
        print("Yritä uudestaan..")
    else:
        break
print("Oikein!")