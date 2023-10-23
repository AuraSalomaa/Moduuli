class Auto:


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








auto1 = Auto("ABC-123", 142, 60, 2000)
print(f"rekisteriosoite on {auto1.rekisteri} ja huippunopeus on {auto1.huippunopeus} km/h")
auto1.kulje(1.5)
#nosto1 = auto1.kiihdyttaa(30)
#nosto2 = auto1.kiihdyttaa(70)
#nosto3 = auto1.kiihdyttaa(50)
#nopeus_nyt = nosto1 + nosto2 + nosto3
#uusin_nopeus = auto1.kiihdyttaa(-200)
#if nopeus_nyt > auto1.huippunopeus:
    #nopeus_nyt = auto1.huippunopeus
#elif uusin_nopeus < 0:
    #uusin_nopeus = 0

#print(f"nykyinen nopeus on {nopeus_nyt}km/h ja jarrutuksen jälkeen nopeus on {uusin_nopeus}km/h")
