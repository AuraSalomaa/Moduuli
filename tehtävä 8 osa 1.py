
import mariadb
import sqlite3
import mysql


yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='admin122!',
    autocommit=True
)
koodi = input("Syötä ICAO koodi: ")
sql = f'SELECT airport.name, airport.municipality FROM airport WHERE airport.ident= "{koodi}"'
yhteys_sql = yhteys.cursor()
yhteys_sql.execute(sql)
tulos = yhteys_sql.fetchall()
print(f"Kentän nimi: " + tulos[0][0])
print(f"Kentän Sijaintikunta: " + tulos[0][1])