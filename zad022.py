import random

def main():
    kol = int(input("Podaj liczbe kolumn: "))
    wie = int(input("Podaj liczbe wierszy: "))
    od = int(input("Podaj przedzial od: "))
    do = int(input("Podaj przedzial do: "))

    tablica = [[random.randint(od, do) for j in range(kol)] for i in range(wie)]
    
    with open("out/danewygenerowane.txt", "w", encoding="utf-8") as plik:
        for i in tablica:
            for j in i:
                print(j, end=", ",file=plik)
            print(file=plik)

try:
    main()
except ValueError:
    print("BLEDNA wartosc liczbowa")
