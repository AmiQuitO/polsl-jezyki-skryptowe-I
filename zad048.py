from math import pi, tan

def PoleWielokata(n: int, a: float) -> float:
    if n < 3:
        raise ValueError("Wielokat musi miec conajmniej 3 boki.")
    if a <= 0:
        raise ValueError("Dlugosc boku musi byc wieksza od 0")

    return (n * (a ** 2)) / (4 * tan(pi/n))

if __name__ == "__main__":
    n = int(input("Podaj liczbe bokow: "))
    a = float(input("Podaj dlugosc boku: "))
    print(f"{PoleWielokata(n, a):.2f}")
