kertaa = 0
while True:

    tunnus = input("Syötä tunnus: ")
    salasana = input("Syötä salasana: ")
    kertaa += 1
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    if kertaa == 5:
        print("Pääsy evätty")
        break
    else:
        print("Väärin meni")

