def rozwiaz_gauss(A, b, eps=1e-8):
    n = len(A)

    if n == 0 or len(b) != n:
        raise ValueError("Niepoprawna liczba równań lub wyrazów wolnych")

    for wiersz in A:
        if len(wiersz) != n:
            raise ValueError("Macierz A musi być kwadratowa")

    M = []

    for i in range(n):
        wiersz = [float(wartosc) for wartosc in A[i]]
        wiersz.append(float(b[i]))
        M.append(wiersz)

    for k in range(n):
        p = k

        for i in range(k + 1, n):
            if abs(M[i][k]) > abs(M[p][k]):
                p = i

        if abs(M[p][k]) < eps:
            raise ValueError("Zerowy lub zbyt mały element główny.\nUkład może nie mieć jednoznacznego rozwiązania.")

        M[k], M[p] = M[p], M[k]

        for i in range(k + 1, n):
            mnoznik = M[i][k] / M[k][k]
            M[i][k] = 0.0

            for j in range(k + 1, n + 1):
                M[i][j] -= mnoznik * M[k][j]

    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0

        for j in range(i + 1, n):
            suma += M[i][j] * x[j]

        x[i] = (M[i][n] - suma) / M[i][i]

    return x


A = [[2, 1],
     [1, -1]]

b = [5, 1]


try:
    wynik = rozwiaz_gauss(A, b)

    for i in range(len(wynik)):
        print(f"x{i + 1} = {wynik[i]:.6f}")

except ValueError as wiadomosc:
    print("Błąd:", wiadomosc)
