with open("in/tekstdostatystyki.txt", "r", encoding="utf-8") as plik:
    with open("out/wersaliki.txt", "w", encoding="utf-8") as plik2:
        plik2.write(plik.read().upper())
