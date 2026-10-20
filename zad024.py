def main():
    liczba = int(input("Podaj liczbe do silni: "))
    if liczba <= 0:
        return
    silnia = 1
    for i in range(1, liczba+1):
        silnia *= i
    return silnia

try:
    print(main())
except ValueError:
    print("BLEDNA wartosc liczbowa")

