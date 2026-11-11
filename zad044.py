def Gauss(A: list[list[int]], b: list[int]) -> list[float]:
    n = len(A)

    if n == 0 or len(b) != n:
        raise ValueError("Niepoprawne wymiary ukladu.")

    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz A musi byc kwadratowa.")

    M = []

    for i in range(n):
        wiersz = [float(element) for element in A[i]]
        wiersz.append(float(b[i]))
        M.append(wiersz)

    eps = 1e-12

    for k in range(n):
        wybrany = k

        for i in range(k + 1, n):
            if abs(M[i][k]) > abs(M[wybrany][k]):
                wybrany = i

        if abs(M[wybrany][k]) < eps:
            raise ValueError(
                "Uklad nie ma jednoznacznego rozwiazania "
                "lub jest numerycznie bliski osobliwemu."
            )

        M[k], M[wybrany] = M[wybrany], M[k]

        for i in range(k + 1, n):
            mnoznik = M[i][k] / M[k][k]

            for j in range(k + 1, n + 1):
                M[i][j] -= mnoznik * M[k][j]

            M[i][k] = 0.0

    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0

        for j in range(i + 1, n):
            suma += M[i][j] * x[j]

        x[i] = (M[i][n] - suma) / M[i][i]

    return x


if __name__ == "__main__":
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]

    b = [8, -11, -3]

    wynik = Gauss(A, b)

    for i, wartosc in enumerate(wynik, start=1):
        print(f"x{i} = {wartosc:.6f}")
