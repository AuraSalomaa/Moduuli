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

maakoodi = input("Syötä maakoodi:" )
sql = f'SELECT type, count(0) FROM airport WHERE airport.iso_country = "{maakoodi}" Group by type'
yhteys_sql = yhteys.cursor()
yhteys_sql.execute(sql)
tulos = yhteys_sql.fetchall()

for i in tulos:
    print(i)