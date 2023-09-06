
import random



def noppa_luku():
    t = random.randint(1, 6)
    return t


while True:
    print(noppa_luku())
    heitto = noppa_luku()
    if heitto == 6:
        break











