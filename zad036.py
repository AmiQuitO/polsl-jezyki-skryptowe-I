def Silnia(a):
    if a == 0:
        return 1
    return Silnia(a-1) * a

try:
    a = int(input("Podaj liczbe calkowita: "))
    if a < 0:
        raise ValueError("Liczba musi byc dodatnia")
    print(Silnia(a))
except ValueError as e: 
    print(f"Podaj poprawna wartosc liczbowa\n{e}")
