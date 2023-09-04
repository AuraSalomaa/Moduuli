lista = []
jarjestetty = []
while True:

    luku = input("Anna luku tai lopeta laittamalla tyhjämerkki: ")

    if luku != "":
        lista.append(luku)
    else:
        lista.sort(reverse=True)
        print(lista[0:5])
        break



