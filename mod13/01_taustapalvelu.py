from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<number>')
def alkuluku(number):
    try:
        jakoluvut = []
        number = int(number)
        for i in range(2, number):
            if number % i == 0:
                jakoluvut.append(i)

        jakolukujen_maara = len(jakoluvut)
        if jakolukujen_maara > 0:
            onko_alkuluku = False
        else:
            onko_alkuluku = True

        tilakoodi = 200
        vastaus = {
            "Number": number,
            "isPrime": onko_alkuluku,
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
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