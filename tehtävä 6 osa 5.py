def parilliset(lista):
    parit = []
    for i in lista:
        if i % 2 == 0:
            parit.append(i)
    return parit


lista2 = [1, 2, 5, 6, 9, 5, 12, 4]
print(lista2)
print(parilliset(lista2))

