class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros
        return kerros

    def kerros_ylos(self, ylospain):
        ylospain += 1
        return ylospain


    def kerros_alas(self,alaspain):
        alaspain -= 1
        return alaspain


h = Hissi(1,10)


kerroksia = h.siirry_kerrokseen(6)
nykyinen_kerros = 0
kysynta = input("Syötä 'up' jos haluat ylös ja 'down' jos haluat mennä alas: ")
if kysynta == "up":
    for i in range(h.alinkerros, h.ylinkerros):
        if i == kerroksia:
            nykyinen_kerros = i
            break
        else:
            if i > h.ylinkerros:
                print(h.ylinkerros)
            elif i < h.alinkerros:
                print(h.alinkerros)
            else:
                print(h.kerros_ylos(i))

elif kysynta == "down":
    for i in range(kerroksia, 1, -1):
            if i > h.ylinkerros:
                print(h.ylinkerros)
            elif i < h.alinkerros:
                print(h.alinkerros)
            else:
                print(h.kerros_alas(i))



