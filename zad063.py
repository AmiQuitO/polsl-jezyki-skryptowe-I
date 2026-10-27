def modul(l):
    if l < 0:
        return -l
    return l


try:
    liczba = int(input("Podaj liczbe z ktorej policzmy modul: "))
    print(modul(liczba))
except ValueError as e:
    print(e)
