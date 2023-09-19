import mariadb
import mysql
import sqlite3
yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='admin122!',
    autocommit=True
)

maakoodi = input("Syötä maakoodi:")
sql = f'SELECT country.name, type, count(0) FROM airport,country WHERE country.iso_country = airport.iso_country and airport.iso_country = "{maakoodi}" Group by type'
yhteys_sql = yhteys.cursor()
yhteys_sql.execute(sql)
tulos = yhteys_sql.fetchall()

for i in tulos:
    print(i)