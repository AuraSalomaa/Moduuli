kuha_pituus = float(input("Syötä kuhan pituus senttimetreissä:"))

if kuha_pituus < 37:
    puuttuu = 37-kuha_pituus
    print(f"Kuha on alamittainen, heitä se takaisin veteen sillä kuhan pituus on {puuttuu} cm alle pyyntirajan")
else:
    print("Kuha on sopivan pituinen!")