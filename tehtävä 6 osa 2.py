import random



def noppa_luku(tahkot):
    sivumaara = random.randint(1, tahkot)
    return sivumaara


suuruus = int(input("Kuinka suuren nopan haluat heittää? "))

while True:
    print(noppa_luku(suuruus))
    heitto = noppa_luku(suuruus)
    if heitto == suuruus:
        break