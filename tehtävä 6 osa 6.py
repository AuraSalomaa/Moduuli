
import math


def pizza_laskuri(mitta_cm, hinta_e):
    laskenta = ((math.pi * mitta_cm) / 100) / 100
    neliohinta = laskenta/hinta_e
    return neliohinta


eka_mitta = float(input("Syötä ensimmäisen pitsan halkaisija cm: "))
eka_hinta = float(input("Syötä ensimmäisen pitsan hinta euroina: "))
ensimmainen = pizza_laskuri(eka_mitta, eka_hinta)

toka_mitta = float(input("Syötä toisen pitsan halkaisija cm: "))
toka_hinta = float(input("Syötä toisen pitsan hinta euroina: "))
toinen = pizza_laskuri(toka_mitta, toka_hinta)

if ensimmainen < toinen:
    print("ensimmäisellä pizzalla on parempi yksikköhinta")
else:
    print("Toisella pizzalla on parempi yksikköhinta ")
