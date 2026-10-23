with open("out/iteracjazsumowaniem.txt", "w", encoding="utf-8") as plik:

    podstawa = int(input("Podaj podstawe: "))

    plik.write(f"{'licznik':>5}  {'suma':>5}\n")
    plik.write(f"{0:*^5}  {0:*^5}\n")
    plik.write(f"-----  -----\n")
    suma = 0

    for i in range(1, 11):
        suma += podstawa
        plik.write(f"{(i):*^5} | {(suma):*^5}\n")


