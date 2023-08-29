lista = []
while True:
    numero = input("Syötä numero tai syötä tyhjä merkki lopettaaksesi: ")
    if numero == '':
        break
    else:
        lista.append(numero)

print(lista)
