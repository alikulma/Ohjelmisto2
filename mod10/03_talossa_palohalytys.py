class Talo:

    hissit = []
    hisseja = 0
    alinkerros = 0
    ylinkerros = 0

    def __init__(self, alin, ylin, hissimaara):
        self.alin = alin
        self.ylin = ylin
        self.hissimaara = hissimaara
        Talo.alinkerros = alin
        Talo.ylinkerros = ylin
        Talo.hisseja = hissimaara + 1
        for i in range(1, Talo.hisseja):
            Talo.hissit.append([i, alin])

    def aja_hissia(self, hissi, kerros):
        print(f"Käytetään hissiä {hissi}.")
        h = Hissi(Talo.alinkerros, Talo.ylinkerros)
        h.siirry_kerrokseen(kerros)
        Talo.hissit[hissi - 1] = [hissi, kerros]

    def palohalytys(self):
        print("Nyt tulee palohälytys! Kaikki hissit palaavat alimpaan kerrokseen.")
        for i in Talo.hissit:
            i[1] = Talo.alinkerros

class Hissi:

    kerros_nyt = 0
    ylinkerros = 0

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        Hissi.kerros_nyt = alin
        Hissi.ylinkerros = ylin

    def kerros_ylos(self):
        Hissi.kerros_nyt += 1
        print(f"Hissi on nyt kerroksessa {Hissi.kerros_nyt}.")

    def kerros_alas(self):
        Hissi.kerros_nyt -= 1
        print(f"Hissi on nyt kerroksessa {Hissi.kerros_nyt}.")

    def siirry_kerrokseen(self, kerros):
        if kerros > Hissi.ylinkerros:
            print("Hissi ei mene noin ylös.")
        else:
            while Hissi.kerros_nyt != kerros:
                if Hissi.kerros_nyt < kerros:
                    Hissi.kerros_ylos(self)
                else:
                    Hissi.kerros_alas(self)

t = Talo(3, 7, 3)
t.aja_hissia(1, 6)
t.aja_hissia(2, 4)
t.palohalytys()
t.aja_hissia(3, 5)