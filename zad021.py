def main():
    liczba = int(input("Podaj liczbe do wypelnienia tabeli: "))

    tabela = [[liczba for j in range(5)] for i in range(7)]

    with open("out/wyjsciezadanie.txt", "w", encoding="utf-8") as plik:
        for i in tabela:
            for j in i:
                print(j, end=", ", file=plik)
            print(file=plik)

try:
    main()
except ValueError:
    print("BLEDNA wartosc liczbowa")
