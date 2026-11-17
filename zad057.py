import random
def Losowy_element_z_pliku():
    with open("in/zad057txt.txt", "r", encoding="utf-8") as plik:
        elementy = plik.read().split()

    if not elementy:
        raise ValueError("Plik nie zawiera elementow")

    return random.choice(elementy)
print(Losowy_element_z_pliku())
