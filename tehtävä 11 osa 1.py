class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, sivumaara, kirjoittaja,  nimi):
        self.sivumaara = sivumaara
        self.kirjoittaja = kirjoittaja
        self.nimi = nimi
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Sivumaara {self.sivumaara} sivua ja Kirjan kirjoittaja on {self.kirjoittaja}")


class Lehti(Julkaisu):
    def __init__(self, paatoimittaja, nimi):
        self.paatoimittaja = paatoimittaja
        self.nimi = nimi
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja on {self.paatoimittaja} ja lehden nimi on {self.nimi}")


julkaisut = []
julkaisut.append(Kirja(200, "Roosa Liksom", "Hytti N:06"))
julkaisut.append(Lehti(" Aki Hyyppä", "Aku ankka"))

for i in julkaisut:
    i.tulosta_tiedot()
