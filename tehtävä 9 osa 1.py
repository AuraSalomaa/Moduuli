class Auto:
    def __init__(self, rekisteri, huippunopeus, sijainti, ajomaara):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.sijainti = sijainti
        self.ajomaara = ajomaara


auto1 = Auto("ABC-123", 142, 0, 0)
print(f"rekisteriosoite on {auto1.rekisteri} ja huippunopeus on {auto1.huippunopeus} km/h")