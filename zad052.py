try:
    z = complex(input("Podaj liczbe zespolona (np. 3+2j): "))
    
    print(f"Modul liczby zespolonej {abs(z)}")

except ValueError:
    print("Niepoprawny zapis. Wpisz np. 3j+2 (bez spacji).")
