import cmath

liczba = float(input("Podaj część urojoną: ").replace(",", "."))
z = complex(0, liczba)

print(f"{cmath.phase(z):.2f}")
