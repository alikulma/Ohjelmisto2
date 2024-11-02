import requests

try:
    input("Paina Enter saadaksesi satunnaisen Chuck Norris -vitsin! ")
    pyynto = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("API ei ole toiminnassa tällä hetkellä.")
