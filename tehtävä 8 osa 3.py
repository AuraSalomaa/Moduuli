import mariadb
import sqlite3
import mysql
from geopy import distance


yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='admin122!',
    autocommit=True
)

lentokentta_1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
lentokentta_2 = input("Syötä toisen lentokentän ICAO-koodi: ")

ensimmainen_lentokentta = f'SELECT longitude_deg, latitude_deg FROM airport WHERE ident = "{lentokentta_1}"'
toinen_lentokentta = f'SELECT longitude_deg, latitude_deg FROM airport WHERE ident = "{lentokentta_2}"'
yhteys_sql = yhteys.cursor()
yhteys_sql.execute(ensimmainen_lentokentta)
tulos1 = yhteys_sql.fetchall()
yhteys_sql.execute(toinen_lentokentta)
tulos2 = yhteys_sql.fetchall()
print(tulos1)
print(tulos2)
etaisyys = distance.distance(tulos1, tulos2).km
print(f"{lentokentta_1} ja {lentokentta_2} ovat toisistaan {etaisyys:.2f} km")
