def Silnia(a):
    if a < 0:
        raise ValueError("Liczba musi byc dodatnia")

    silnia = 1

    for i in range(1, a+1):
        silnia *= i

    return silnia

try:
    a = int(input("Podaj liczbe calkowita: "))
    print(f"Silnia z !{a} wynosi {Silnia(a)}")
except ValueError as e: 
    print(f"Podaj poprawna wartosc liczbowa\n{e}")
