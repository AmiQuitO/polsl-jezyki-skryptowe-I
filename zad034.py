plcie = ["Kobieta", "Mezczyzna"]
kolory = ["bialy", "czarny", "zielony", "czerwony", "niebieski", "zolty", "szary"]
rozmiary = ["XXL", "XL", "L", "M", "S", "XS"]

i = 1

for p in plcie:
    for k in kolory:
        for r in rozmiary:
            with open(f"out/zad034/metka_{i}.txt", "w", encoding="utf-8") as plik:
                plik.write(f"{p}, {k}, {r}")
                i += 1
