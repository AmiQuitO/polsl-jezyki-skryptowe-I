from zad038 import Sortowanie_babelkowe, Sortowanie_przez_wstawianie, Sortowanie_szybkie
from time import perf_counter
from statistics import mean, pstdev
from datetime import date


with open("in/zad040txt.txt", "r", encoding="utf-8") as plik:
    liczby = [int(x) for x in plik.readlines()]

czas_babelkowe = []
czas_przez_wstawianie = []
czas_szybkie = []

ile = 5

for _ in range(ile):
    l = liczby.copy()
    start = perf_counter()
    Sortowanie_babelkowe(l)
    czas = perf_counter() - start
    czas_babelkowe.append(czas)

for _ in range(ile):
    l = liczby.copy()
    start = perf_counter()
    Sortowanie_przez_wstawianie(l)
    czas = perf_counter() - start
    czas_przez_wstawianie.append(czas)

for _ in range(ile):
    l = liczby.copy()
    start = perf_counter()
    Sortowanie_szybkie(l)
    czas = perf_counter() - start
    czas_szybkie.append(czas)

nazwa = f"out/raport_{date.today():%Y-%m-%d}.txt"

with open(nazwa, "w", encoding="utf-8") as plik:
    plik.write("RAPORT ALGORYTMÓW SORTOWANIA\n\n")
    plik.write(
            f"-- {"NAZWA":->10} -- LICZBA SORTOWANYCH PLIKOW -- SREDNI CZAS -- ODCHYLENIE STANDARDOWE\n"
    )

    plik.write(
        f"1. babelkowe -- {len(czas_babelkowe)} -- "
        f"{mean(czas_babelkowe):.6f} s -- {pstdev(czas_babelkowe):.6f} s\n"
    )

    plik.write(
        f"2. przez wstawianie -- {len(czas_przez_wstawianie)} -- "
        f"{mean(czas_przez_wstawianie):.6f} s -- {pstdev(czas_przez_wstawianie):.6f} s\n"
    )
    plik.write(
        f"3. szybkie -- {len(czas_szybkie)} -- "
        f"{mean(czas_szybkie):.6f} s -- {pstdev(czas_szybkie):.6f} s\n"
    )
