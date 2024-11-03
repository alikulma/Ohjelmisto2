import requests

try:
    kaupunki = input("Kirjoita paikkakunnan nimi, josta haluat säätiedot: ")
    api_key = "1234"
    cords_pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=5&appid={api_key}"
    cords_vastaus = requests.get(cords_pyynto)
    json_cords_vastaus = cords_vastaus.json()
    lat = json_cords_vastaus[0]["lat"]
    lon = json_cords_vastaus[0]["lon"]
    saa_pyynto = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=fi&appid={api_key}"
    saa_vastaus = requests.get(saa_pyynto)
    json_saa_vastaus = saa_vastaus.json()
    if cords_vastaus.status_code == 200 and saa_vastaus.status_code == 200:
        saatila = json_saa_vastaus["weather"][0]["description"]
        lampotila = json_saa_vastaus["main"]["temp"]
        print(f"Paikkakunnalla {kaupunki} sään kuvaus on '{saatila}' ja lämpötila on {lampotila} celsiusta.")
except requests.exceptions.RequestException as e:
    print("API ei ole toiminnassa tällä hetkellä.")
