import requests

kayttaja_vastaus = ""

try:
    search = "https://api.chucknorris.io/jokes/random"
    tulos = requests.get(search)
    if tulos.status_code == 200:
        onnistunut = tulos.json()
        print(f"vitsi: {onnistunut['value']}")
except requests.exceptions.RequestException as e:
    print("Haku epäonnistui verkkovirheen tai muun vian takia. Pahoittelen :(")


