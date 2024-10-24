class Auto:
    nopeus_nyt = 0
    kuljettu_matka = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus {auto.huippunopeus} km/h.")
print(f"Se on kulkenut tähän mennessä {Auto.kuljettu_matka} km ja sen nopeus tällä hetkellä on {Auto.nopeus_nyt} km/h.")