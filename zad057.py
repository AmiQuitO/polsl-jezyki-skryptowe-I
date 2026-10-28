import random
with open("in/zad057txt.txt", "r", encoding="utf-8") as plik:
    print(random.choice(plik.read().split()))

