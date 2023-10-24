import random


class Auto:
    import random

    def __init__(self, rekisteri, huippunopeus, nopeus, ajomaara):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.ajomaara = ajomaara

    def kiihdyttaa(self, kiihdytys: int):
        muutos = self.nopeus + kiihdytys
        return muutos

    def kulje(self, tuntimaara):
        ajomaara = self.ajomaara
        nopeus = self.nopeus
        ajettu_matka = (nopeus * tuntimaara)+ajomaara
        print(f"{ajettu_matka:.0f} km")
        return

kerrat = 0
osallistujat = []
for i in range(10):
    kerrat += 1
    Rekisteri = f"ABC-{kerrat}"
    Suurin_nopeus = random.randint(100, 200)
    auto1 = Auto(Rekisteri, Suurin_nopeus, 0, 0)
    osallistujat.append(auto1)

print(osallistujat)
#print(f"rekisteriosoite on {auto1.rekisteri} ja huippunopeus on {auto1.huippunopeus} km/h")
#auto1.kulje(1.5)