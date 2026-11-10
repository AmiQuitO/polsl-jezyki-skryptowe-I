def Utworz_Kody(tekst: str) -> dict[str, str]: 
    if not tekst: return {} 
    wystapienia = {}
    for x in tekst:
        if x not in wystapienia:
            wystapienia[x] = tekst.count(x)

    w = sorted(wystapienia.items(), key=lambda para: (-para[1], para[0]))

    kody = {}

    def podziel(grupa, prefiks):

        if len(grupa) == 1:
            z = grupa[0][0]
            kody[z] = prefiks or "0"
            return

        suma = sum(liczba for znak, liczba in grupa)
        
        suma_l = 0
        najlepszy_podzial = 1
        najmniejsza_roznica = float("inf")

        for i in range(1, len(grupa)):
            suma_l += grupa[i-1][1]
            suma_p = suma - suma_l

            roznica = abs(suma_p - suma_l)

            if roznica < najmniejsza_roznica:
                najmniejsza_roznica = roznica
                najlepszy_podzial = i

        podziel(grupa[:najlepszy_podzial], prefiks + "0")
        podziel(grupa[najlepszy_podzial:], prefiks + "1")

    podziel(w, "")

    return kody

def Koduj(tekst: str) -> tuple:
    kody = Utworz_Kody(tekst)
    bity = "".join(kody[z] for z in tekst)

    return bity, kody

def Dekoduj(bity, kody):
    odwrotne_kody = {kod: znak for znak, kod in kody.items()}

    prefiksy = {
            kod[:i]
            for kod in odwrotne_kody
            for i in range(1, len(kod) + 1)
            }

    wynik = []
    fragment = ""

    for bit in bity:
        if bit not in "01":
            raise ValueError("Zakodowany tekst moze zawierac wylacznie 0 i 1")

        fragment += bit

        if fragment in odwrotne_kody:
            wynik.append(odwrotne_kody[fragment])
            fragment = ""
        elif fragment not in prefiksy:
            raise ValueError("Ciag bitow nie pasuje do slownika bitow")

    if fragment:
        raise ValueError("Niepelny kod na koncu ciagu bitow")

    return "".join(wynik)

if __name__ == "__main__":
    tekst = str(input("Podaj tekst do zakodowania: "))

    bit_a, kod_a = Koduj(tekst)
    print(bit_a, kod_a)

    b = Dekoduj(bit_a, kod_a)
    print(b)
