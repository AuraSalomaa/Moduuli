lista = set(())
tyhja = "o"
while tyhja != "":
    nimi = input("Syötä nimiä, tyhjä merkki lopettaa: ")
    tyhja = nimi

    if nimi in lista:
        print("Nimi on aiemmin syötetty")
    else:
        print("Uusi nimi")
        lista.add(nimi)

for i in lista:
    print(i)

