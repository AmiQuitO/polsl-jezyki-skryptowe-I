def Pobierz():
    liczba = input("Podaj liczbe calkowita: ")

    try:
        liczba = int(liczba)
        return f"{type(liczba).__name__} - {liczba}"
    except ValueError:
        pass


    try:
        liczba = float(liczba)
        return f"{type(liczba).__name__} - {liczba}"
    except ValueError:
        pass
    
    try:
        liczba = complex(liczba)
        return f"{type(liczba).__name__} - {liczba}"
    except ValueError:
        return "Podany tekst nie jest poprawna liczba"

print(Pobierz())
