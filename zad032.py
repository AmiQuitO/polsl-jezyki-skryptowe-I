import cmath

def Rownanie_kwadratowe(a, b, c):
    
    delta = b ** 2 - 4 * a * b

    x1 = (-b - cmath.sqrt(delta)) / (2 * a)
    x2 = (-b + cmath.sqrt(delta)) / (2 * a)

    return x1, x2


with open("in/wspolczynniki.txt", "r", encoding="utf-8") as plik:
    wsp = [complex(x) for x in plik.read().split()]

if len(wsp) != 3:
    raise ValueError("Plik musi zawierac dokladnie 3 wspolczynniki: a, b, c.")

x1, x2 = Rownanie_kwadratowe(wsp[0], wsp[1], wsp[2])

print(f"{wsp[0]}x^2 + {wsp[1]}x + {wsp[2]}\nx1 = {x1}\nx2 = {x2}")
