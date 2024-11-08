from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='käyttäjänimi',
    password='salasana',
    autocommit=True
)

app = Flask(__name__)
@app.route('/kenttä/<koodi>')
def kentta(koodi):
    try:
        sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}';"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        vastaus = {
            "ICAO": koodi,
            "Name": tulos[0][0],
            "Municipality": tulos[0][1]
        }

        tilakoodi = 200


    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO-koodi"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)