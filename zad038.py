
def Sortowanie_babelkowe(l: list[int]):
    sort = False
    i = 0
    while True:
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            sort = False
        i += 1
        if i == len(l)-1:
            i = 0
            if sort:
                break
            sort = True
    return l

def Sortowanie_przez_wstawianie(l: list[int]):
    nowa_lista: list[int] = []

    for liczba in l:
        i = 0

        while i < len(nowa_lista) and nowa_lista[i] < liczba:
            i += 1

        nowa_lista.insert(i, liczba)

    return nowa_lista

def Sortowanie_szybkie(l: list[int]):
    if len(l) <= 1:
        return l
    pivot = l[len(l)//2]
    rowne: list[int] = []
    wieksze: list[int] = []
    mniejsze: list[int] = []
    for liczba in l:
        if liczba < pivot:
            mniejsze.append(liczba)
        elif liczba == pivot:
            rowne.append(liczba)
        else:
            wieksze.append(liczba)
    return Sortowanie_szybkie(mniejsze) + rowne + Sortowanie_szybkie(wieksze)

if __name__ == "__main__":
    lista: list[int]
    with open("in/zad038txt.txt", "r", encoding="utf-8") as plik:
        lista = [int(x) for x in plik.read().split()]

    print(lista)
    print(f"Sortowanie babelkowe: \n{Sortowanie_babelkowe(lista.copy())}")
    print(f"Sortowanie przez wstawianie: \n{Sortowanie_przez_wstawianie(lista.copy())}")
    print(f"Srotowanie szybkie: \n{Sortowanie_szybkie(lista.copy())}")

    with open("out/zad038txt.txt", "w", encoding="utf-8") as plik:
        print(f"Sortowanie babelkowe: {Sortowanie_babelkowe(lista.copy())}", file=plik)
        print(f"Sortowanie przez wstawianie: {Sortowanie_przez_wstawianie(lista.copy())}", file=plik)
        print(f"Srotowanie szybkie: {Sortowanie_szybkie(lista.copy())}", file=plik)
