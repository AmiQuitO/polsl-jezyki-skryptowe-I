liczba = int(input("Podaj liczbe do wypelnienia tabeli: "))

tabela = [[liczba for j in range(5)] for i in range(7)]

for i in tabela:
    for j in i:
        print(j, end=", ")
    print()

