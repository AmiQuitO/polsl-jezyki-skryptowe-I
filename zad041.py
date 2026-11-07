def Szyfr_Cezara(ciag: str, ile: int, alfabet: str) -> str:
    if not alfabet:
        raise ValueError("Alfabet nie może być pusty")

    szyfr = ""

    for znak in ciag:
        if znak == " ":
            szyfr += znak
            continue

        mala_litera = znak.lower()

        if mala_litera not in alfabet:
            raise ValueError(f"Znak nie istnieje w alfabecie: {znak!r}")

        idx = (alfabet.index(mala_litera) + ile) % len(alfabet)
        nowy_znak = alfabet[idx]

        if znak.isupper():
            nowy_znak = nowy_znak.upper()

        szyfr += nowy_znak

    return szyfr


alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
ciag = "Witam wszystkich"
ile = 4

nowy_ciag = Szyfr_Cezara(ciag, ile, alfabet)
odszyfrowany = Szyfr_Cezara(nowy_ciag, -ile, alfabet)

print(f"Szyfrowanie: {ciag} -> {nowy_ciag}")
print(f"Deszyfrowanie: {nowy_ciag} -> {odszyfrowany}")
