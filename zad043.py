class Wezel:
    def __init__(self, liczba, znak=None, lewy=None, prawy=None):
        self.liczba = liczba
        self.znak = znak
        self.lewy = lewy
        self.prawy = prawy


def Utworz_Kody(tekst: str) -> dict[str, str]:
    if not tekst:
        return {}

    wystapienia = {}

    for znak in tekst:
        if znak not in wystapienia:
            wystapienia[znak] = 0

        wystapienia[znak] += 1

    wezly = []

    for znak, liczba in wystapienia.items():
        wezly.append(Wezel(liczba, znak))

    while len(wezly) > 1:
        wezly = sorted(wezly, key=lambda wezel: wezel.liczba)

        lewy = wezly.pop(0)
        prawy = wezly.pop(0)

        rodzic = Wezel(
            liczba=lewy.liczba + prawy.liczba,
            lewy=lewy,
            prawy=prawy,
        )

        wezly.append(rodzic)

    korzen = wezly[0]
    kody = {}

    def przypisz_kody(wezel, prefiks):
        if wezel.znak is not None:
            kody[wezel.znak] = prefiks or "0"
            return

        przypisz_kody(wezel.lewy, prefiks + "0")
        przypisz_kody(wezel.prawy, prefiks + "1")

    przypisz_kody(korzen, "")

    return kody


def Koduj(tekst: str) -> tuple[str, dict[str, str]]:
    kody = Utworz_Kody(tekst)
    bity = "".join(kody[znak] for znak in tekst)

    return bity, kody


def Dekoduj(bity: str, kody: dict[str, str]) -> str:
    odwrotne_kody = {
        kod: znak
        for znak, kod in kody.items()
    }

    wynik = []
    aktualny_kod = ""

    for bit in bity:
        if bit not in "01":
            raise ValueError("Zakodowany tekst moze zawierac tylko 0 i 1.")

        aktualny_kod += bit

        if aktualny_kod in odwrotne_kody:
            wynik.append(odwrotne_kody[aktualny_kod])
            aktualny_kod = ""

    if aktualny_kod:
        raise ValueError("Niepelny lub niepoprawny ciag bitow.")

    return "".join(wynik)

if __name__ == "__main__":
    tekst = "BANANA"

    bity, kody = Koduj(tekst)
    odkodowany = Dekoduj(bity, kody)

    print("Tekst:", tekst)
    print("Kody:", kody)
    print("Zakodowany:", bity)
    print("Odkodowany:", odkodowany)

