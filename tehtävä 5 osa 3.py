luku = int(input("Syötä alkuluku: "))
if luku > 1:
    for i in range(2, luku):

        if luku % i == 0:
            print(f"{luku} ei ole alkuluku")
            break
else:
    print(f"{luku} on alkuluku")







