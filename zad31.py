with open("out/iteracjazsumowaniem.txt", "w", encoding="utf-8") as plik:

    podstawa = int(input("Podaj podstawe: "))

    print(f"{'licznik':>5}  {'suma':>5}")
    print(f"{0:*^5}  {0:*^5}")
    print(f"-----  -----")
    suma = 0

    for i in range(1, 11):
        suma += podstawa
        print(f"{(i):*^5} | {(suma):*^5}")


