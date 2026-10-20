with open("in/danezadanie.txt", "r", encoding="utf-8") as plik:
    liczba = int(plik.read())

with open("out/liczbykonwertowane.txt", "w", encoding="utf-8") as plik:
    plik.write(f"{liczba}, {hex(liczba)}, {oct(liczba)}")
