import math

class Kolo():
    def __init__(self, r:float) -> None:
        self.r = r
    def pole(self):
        return math.pi * self.r * self.r
    def dlugosc_okregu(self):
        return 2 * math.pi * self.r
    def obwod(self):
        return 2 * math.pi * self.r

k = Kolo(5)

print(f"Pole wynosi: {k.pole():.4f}")
print(f"Dlugosc okregu wynosi: {k.dlugosc_okregu():.4f}")
print(f"Obwod wynosi: {k.obwod():.4f}")
