class Ciag():
    def __init__(self, ciag) -> None: 
        self.ciag = ciag
    def odwroc(self):
        lista_ciag = self.ciag.split()
        nowy_ciag = lista_ciag[::-1]
        self.ciag = " ".join(nowy_ciag)
    def get_ciag(self):
        return self.ciag

zdanie = Ciag("Jestem studentem. Jestem studentem.")
print(zdanie.get_ciag())
zdanie.odwroc()
print(zdanie.get_ciag())
