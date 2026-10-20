while True:
    try:
        liczba = int(input("Podaj calkowita: "))
        break
    except ValueError:
        print("BLAD - Podana liczba nie jest liczba calkowita - Sprobuj ponownie.")

print(f"Podana liczba to {liczba}")
