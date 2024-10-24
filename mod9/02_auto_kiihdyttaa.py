class Auto:
    nopeus_nyt = 0
    kuljettu_matka = 0

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    def kiihdyta(self, nopeuden_muutos):
        Auto.nopeus_nyt += nopeuden_muutos
        if Auto.nopeus_nyt < 0:
            Auto.nopeus_nyt = 0
        elif Auto.nopeus_nyt > self.huippunopeus:
            Auto.nopeus_nyt = self.huippunopeus
        return


auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus {auto.huippunopeus} km/h.")
print(f"Se on kulkenut tähän mennessä {Auto.kuljettu_matka} km ja sen nopeus tällä hetkellä on {Auto.nopeus_nyt} km/h.")
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus tällä hetkellä on {Auto.nopeus_nyt} km/h.")
auto.kiihdyta(-200)
print(f"Auton nopeus tällä hetkellä on {Auto.nopeus_nyt} km/h.")