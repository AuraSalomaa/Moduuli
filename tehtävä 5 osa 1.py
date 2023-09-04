import random
lista = []
noppa_arpa = int(input("Anna noppa luku, niin heitän sen verran noppia: "))

for i in range(noppa_arpa):
    arpoja = random.randint(1, 6)
    lista.append(arpoja)
    print(lista)

print(sum(lista))