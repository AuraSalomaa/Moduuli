import math
import random
name = input("Mikä on nimesi?")
circle = int(input("Syötä ympyrän säde:"))
width = int(input("Syötä leveys:"))
hight = int(input("syötä korkeus:"))
a = int(input("anna ensimmäinen numero:"))
b = int(input("anna toinen numero:"))
c = int(input("anna kolmas numero:"))
luodit = float(input("anna luodit:"))
naulat = int(input("anna naulat:"))
leiviskat = int(input("anna leiviskat:"))
kolmenumero_koodi = random.sample(range(1,9),3)
nelinumero_koodi  = random.sample(range(1,6),4)
CircleArea = circle * circle * math.pi
squareArea = width * hight
squareAround = (width * width) + (hight + hight)
keskiarvo = a + b + c /3
summa = a + b + c
tulo = a * b * c
sievennetty = (keskiarvo)
luoti = 13.30
naula = 32 * luoti
leiviska = naula * 20
lasku = (leiviska * leiviskat) + (naula * naulat) + (luoti * luodit)
osa = '{:,}'.format(lasku)
osat = osa.split(",",1 )
print(f"Terve {name}!ln.Antamasi ympyrän mitan pinta-ala on {CircleArea}.ln Suorakulmiosi pinta-ala on{squareArea} ja suorakulmion piiri.{squareAround}.")
print(f"antamiesi numeroiden keskiarvo{sievennetty}, summa {summa} ja tulo ovat tässä{tulo}.Kilogrammaa {osat[0]}, grammaa {osat[1]} ")
print(f"Antamiesi tietojen nykyinen paino on {osat[0]} kg ja {osat[1]} grammaa")
print(f"Lopuksi tässä sinulle tarvittavat koodit numero lukkoihin kolmenumeroinen {kolmenumero_koodi} ja lisäksi nelinumeroinen koodi {nelinumero_koodi}")