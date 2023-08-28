Biologinen_sukupuoli = input("Syötä biologinen sukupuolesi:")
Hemoglobiini_arvo = int(input("Hemoglobiini arvot tyyliä(g/l):"))

if Biologinen_sukupuoli == "Nainen":
    if Hemoglobiini_arvo < 117:
        print("Hemoglobiini arvot alhaiset")
    elif 117 <= Hemoglobiini_arvo <= 175:
        print("Hemoglobiini arvot normaalit")

    else:
        print("Hemoglobiini arvot korkeat")

elif Biologinen_sukupuoli == "Mies":
    if Hemoglobiini_arvo < 134:
        print("Hemoglobiini arvot alhaiset")
    elif 134 <= Hemoglobiini_arvo <= 195:
        print("Hemoglobiini arvot normaalit")
    else:
        print("Hemoglobiini arvot Korkeat")

