def bensiinin_maara(bensiini):
    litrat = bensiini * 3.785
    return litrat


while True:
    gallonia_usa = int(input("Syötä usa:n gallonia niin saat litroina tuloksen: "))
    print(bensiinin_maara(gallonia_usa))
    if gallonia_usa < 0:
        break