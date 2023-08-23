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
kolmenumero_koodi = random.randint(1,9)
nelinumero_koodi  = random.randint(1,6)
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
print(kolmenumero_koodi,kolmenumero_koodi,kolmenumero_koodi)
print(f"Terve {name}!. {CircleArea}. {squareArea} ja {squareAround}.{sievennetty} {summa} {tulo}.Kilogrammaa {osat[0]}, grammaa {osat[1]} ")

