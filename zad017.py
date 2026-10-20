def Pobierz():
    try:
        return int(input("Podaj liczbe calkowita: "))
    except ValueError:
        return "Nie wprowadziles liczby calkowitej"

print(Pobierz())
