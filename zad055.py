class GeneratorLCG():
    def __init__(self, seed) -> None:
        self.a = 1234567
        self.c = 567891234
        self.m = 2**32
        self.stan = seed % self.m
    def losuj(self):
        self.stan = (self.a * self.stan + self.c) % self.m
        return self.stan

generator = GeneratorLCG(2233343)   

for i in range(10):
    print(generator.losuj())
