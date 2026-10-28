def na_rzymska(liczba):
    if not 1 <= liczba <= 3999:
        raise ValueError("Podaj liczbę od 1 do 3999.")

    symbole = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    wynik = ""

    for wartosc, symbol in symbole:
        while liczba >= wartosc:
            wynik += symbol
            liczba -= wartosc

    return wynik

try:
    liczba = int(input("Podaj liczbę całkowitą od 1 do 3999: "))
    print(f"Zapis rzymski: {na_rzymska(liczba)}")
except ValueError as e:
    print(f"Niepoprawne dane: {e}")
