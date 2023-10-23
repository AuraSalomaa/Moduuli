class Auto:


    def __init__(self, rekisteri, huippunopeus, nopeus, ajomaara):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.ajomaara = ajomaara

    def kiihdyttaa(self, kiihdytys: int):
        muutos = self.nopeus + kiihdytys
        return muutos










auto1 = Auto("ABC-123", 160, 0, 0)
print(f"rekisteriosoite on {auto1.rekisteri} ja huippunopeus on {auto1.huippunopeus} km/h")
nosto1 = auto1.kiihdyttaa(30)
nosto2 = auto1.kiihdyttaa(70)
nosto3 = auto1.kiihdyttaa(50)
nopeus_nyt = nosto1 + nosto2 + nosto3
uusin_nopeus = auto1.kiihdyttaa(-200)
if nopeus_nyt > auto1.huippunopeus:
    nopeus_nyt = auto1.huippunopeus
elif uusin_nopeus < 0:
    uusin_nopeus = 0

print(f"nykyinen nopeus on {nopeus_nyt}km/h ja jarrutuksen jälkeen nopeus on {uusin_nopeus}km/h")


