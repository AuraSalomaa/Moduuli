
while True:
    muuntaja = float(input("Syötä senttimetrejä niin saat tuloksen tuumina: "))
    if muuntaja < 0:
        break
    else:
        tuuma = muuntaja * 2.54
        print(tuuma)