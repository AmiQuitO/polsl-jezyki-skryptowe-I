class Matematyka():
    def pow(self, x: float, n):
        wynik = 1
        for i in range(abs(n)):
            if n < 0:
                wynik /= x
            else:
                wynik *= x
        return wynik

M = Matematyka()

print(M.pow(5, -3))
print(M.pow(5, -2))
print(M.pow(5, -1))
print(M.pow(5, 0))
print(M.pow(5, 1))
print(M.pow(5, 2))
print(M.pow(5, 3))

