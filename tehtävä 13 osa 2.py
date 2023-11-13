import mariadb
import mysql
import sqlite3
from flask import Flask, request

app = Flask(__name__)


yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='admin122!',
    autocommit=True
)


@app.route('/Lentokentta')
def lentokentta_haku():

        args = request.args
        maakoodi = str(args.get("maakoodi"))
        sql = f'SELECT airport.name, airport.ident, Municipality FROM airport WHERE ident = {maakoodi} '
        yhteys_sql = yhteys.cursor()
        yhteys_sql.execute(sql)
        tulos = yhteys_sql.fetchall()
        status_code = 200

        vastaus = {
            "maakoodi ": maakoodi

            }
        return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
