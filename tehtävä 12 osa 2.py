import requests
api_key = "4c166ab153b1f9256c3cc92b5c0e5519"
Kaupunki = input("Syötä kaupunki: ")

try:
    search = f"https://api.openweathermap.org/data/2.5/weather?q={Kaupunki}&appid={api_key}"
    tulos = requests.get(search)
    if tulos.status_code == 200:
        onnistunut_haku = tulos.json()
        kuvailu = onnistunut_haku['weather'][0]['description']
        celsius = onnistunut_haku['main']['temp'] - 273.73
        print(f"Säätila {kuvailu}")
        print(f"Kaupungissa {Kaupunki} lämpötila on {celsius:.1f} Celsius astetta. ")
except requests.exceptions.RequestException as e:
    print("Haku ei onnistunut mahdollisen verkkohäiriön vuoksi, pahoittelen tätä :(")

