class Auto:
    nopeus_nyt = 60
    kuljettu_matka = 2000

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

    def kulje(self, tunnit):
        Auto.kuljettu_matka = Auto.kuljettu_matka + Auto.nopeus_nyt * tunnit
        return


auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus {auto.huippunopeus} km/h.")
print(f"Se on kulkenut tähän mennessä {Auto.kuljettu_matka} km ja sen nopeus tällä hetkellä on {Auto.nopeus_nyt} km/h.")
print("Auto kulkee 1,5 tuntia.")
auto.kulje(1.5)
print(f"Se on kulkenut tähän mennessä {Auto.kuljettu_matka} km ja sen nopeus tällä hetkellä on {Auto.nopeus_nyt} km/h.")