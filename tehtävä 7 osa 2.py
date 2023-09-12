lista = set(())

while True:
    nimi = input("Syötä nimiä, tyhjä merkki lopettaa: ")
    if nimi == "":
        break
    else:
        if nimi in lista:
            print("Nimi on aiemmin syötetty")
        else:
            print("Uusi nimi")
            lista.add(nimi)

for i in lista:
    print(i)

