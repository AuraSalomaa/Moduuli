class Hissi:
    kysynta = input("Up or down ?")

    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros



    def kerros_ylos(self):

        return + 1


    def kerros_alas(self):

        return - 1

    def siirry_kerrokseen(self, kerros):
        if Hissi.kysynta == "up":
            for i in range(kerros):
                print(i + self.kerros_ylos())

        elif Hissi.kysynta == "down":
            for i in range(kerros, self.alinkerros, -1):
                print(i - self.kerros_alas())




h = Hissi(0,10)
kerroksia = h.siirry_kerrokseen(6)
