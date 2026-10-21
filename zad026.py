import math

def main():

    print("========= Suma i roznica kwadratow =========")

    print("Alfa - 60, Beta - 30")
    sl, sp, rl, rp = Suma_i_roznica_kwadratow(60, 30)
    print(f"Suma lewa - {sl}\nSuma prawa - {sp}\nRoznica lewa - {rl}\nRoznica prawa - {rp}")
    print(f"Zgodnosc sumy: {math.isclose(sl, sp, abs_tol=1e-12)}")
    print(f"Zgodnosc roznicy: {math.isclose(rl, rp, abs_tol=1e-12)}")

    print("============= Dwumian Newtona =============")
    x = 2
    n = 3
    print(f"Z rozwiniecia: {Dwumian_newtona(x, n)}\nBezposrednio: {(1 + x) ** n}")

    print("=== Pierwiastki z rownania kwadratowego ===")
    a = 2
    b = 4
    c = 0
    print(f"Miejsca zerowe dla {a}x^2 + {b}x + {c}: {Pierwiastki_kwadratowe(a, b, c)}")
    
    
    print("============ Przyblizenie e^x ============")
    
    X = 1
    N = 10
    
    z_szeregu = Przyblizenie_e(X, N)

    print(f"Z szeregu: {z_szeregu}\nZ math.exp: {math.exp(X)}\nBlad bezwzgledny: {math.isclose(z_szeregu, math.exp(X), abs_tol=1e-5)}")

    print("============ Szereg Fouriera ============")
    
    print(f"Wartosc sumy czesciowej: {Szereg_Fouriera(0, math.pi, 1, [2, 3], [4, 5])}")


def Suma_i_roznica_kwadratow(alfa_stopnie, beta_stopnie):

    alfa = math.radians(alfa_stopnie)
    beta = math.radians(beta_stopnie)

    suma_lewa = math.sin(alfa) + math.sin(beta)
    suma_prawa = 2 * math.sin((alfa + beta) / 2) * math.cos((alfa - beta) / 2)


    roznica_lewa = math.sin(alfa) - math.sin(beta)
    roznica_prawa = 2 * math.sin((alfa - beta) / 2) * math.cos((alfa + beta) / 2)

    return suma_lewa, suma_prawa, roznica_lewa, roznica_prawa


def Dwumian_newtona(x, n):

    if n < 0:
        raise ValueError("n musi byc liczba dodatnia calkowita")
    suma = 0

    for k in range(n+1):
        s = math.comb(n, k) * x ** k
        suma += s
    
    return suma



def Pierwiastki_kwadratowe(a, b, c):

    delta = b**2 - (4*a*c)

    if delta < 0:
        return None
    elif delta == 0:
        return (-b) / (2*a)
    else:
        return ((-b) + math.sqrt(delta)) / (2*a), ((-b) - math.sqrt(delta)) / (2*a)


def Przyblizenie_e(x, n):
    
    if n < 0:
        raise ValueError("n musi byc nieujemne")

    suma = 0

    for k in range(n + 1):
        s = x ** k / math.factorial(k)
        suma += s

    return suma



def Szereg_Fouriera(x, L, a0, a, b):
    
    if L <= 0:
        raise ValueError("L musi byc dodatnie")
    
    if len(a) != len(b):
        raise ValueError("Listy a 0 b musza miec taka sama dlugosc")

    suma = a0
    N = len(a)

    for n in range(0, N):
        argument = (n+1) * math.pi * x / L

        skladnik = (a[n] * math.cos(argument) + b[n] * math.sin(argument))
        
        suma += skladnik

    return suma


    

main()
