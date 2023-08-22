name = input("Mikä on nimesi?")
circle = int(input("Syötä ympyrän säde:"))
width = int(input("Syötä leveys:"))
hight = int(input("syötä korkeus:"))
CircleArea = circle * circle * 3.14
squareArea = width * hight
squareAround = (width * width) + (hight + hight)

print(f"Terve {name}!. {CircleArea}. {squareArea} ja {squareAround}")

