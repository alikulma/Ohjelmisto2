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

h = Hissi(1, 6)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)