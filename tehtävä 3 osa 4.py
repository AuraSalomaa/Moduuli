vuosi = int(input("Anna vuosi:"))

if vuosi % 100 and vuosi % 400 == 0:
    print(f"{vuosi} on karkausvuosi")
elif vuosi % 4 == 0 and vuosi % 100 != 0:
    print(f"{vuosi} on karkausvuosi")

else:
    print(f"{vuosi} ei ole karkausvuosi")
