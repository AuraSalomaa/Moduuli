kuukausi = int(input("Syötä kuukauden numero(1-12): "))
kuukaudet = ("Talvi", "Kevät","Kesä", "Syksy")

if 3 <= kuukausi <= 5:
    print(kuukaudet[1])
elif 6 <= kuukausi <= 8:
    print(kuukaudet[2])
elif 9 <= kuukausi <= 11:
    print(kuukaudet[3])
else:
    print(kuukaudet[0])

