try:
    z1 = complex(input("Podaj 1 liczbe zespolona (np. 3+2j): "))
    z2 = complex(input("Podaj 2 liczbe zespolona (np. 3+2j): "))
    
    print(f"Iloraz: {z1 / z2}")

except ValueError:
    print("Niepoprawny zapis. Wpisz np. 3j+2 (bez spacji).")
except ZeroDivisionError:
    print("Dzielenie przez 0")
