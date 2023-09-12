Lentokentta_koodeja = {"OSA": "Osaka, Japani", "PEK": "Beijing Capital International", "ARN": "Arlanda"}
merkki = ""
while merkki != "lopeta":
    print("Syötä (uusi) lisätäksesi uuden lentoaseman, (haku)hakeaksi aiemmin syötetyn tai (lopeta) lopettaaksesi\n")
    kysynta = input("Mitä haluat tehdä? ")
    merkki = kysynta
    if kysynta == "uusi":
        koodi = input("Syötä lentokenttä koodi: ")
        kaupunki = input("Syötä lentokentän nimi: ")
        Lentokentta_koodeja[koodi] = f"{kaupunki}"
    elif kysynta == "haku":
        ICAO_koodi= input("Syötä lentokentän ICAO-koodi: ")
        print(Lentokentta_koodeja[ICAO_koodi])

print("Kiitos käynnista ja tervetuloa uudelleen! :-)")