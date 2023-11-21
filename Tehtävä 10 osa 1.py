class Hissi:

    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros

        return kerros

    def kerros_ylos(self):
        ylos = 0
        for i in range(self.alinkerros, self.kerros):
            if ylos != self.ylinkerros:
                ylos += 1
                print(ylos)

            else:
                print(self.ylinkerros)


    def kerros_alas(self):
        alas = self.ylinkerros
        for i in range(self.ylinkerros, self.kerros, -1):
            if alas != self.alinkerros:
                alas -= 1
                print(alas)
            else:
                print(self.alinkerros)






h = Hissi(0,10)


kerroksia = h.siirry_kerrokseen(5)
h.kerros_alas()
