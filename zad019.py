import random

def main():
    try:
        od = int(input("Podaj poczatek przedzialu: "))
        do = int(input("Podaj koniec przedzialu: "))

        if od > do:
            print("Podany przedzial jest niepoprawny")
            return
        
        liczba = random.randint(od,do)

        with open("in/zad019txt.txt", "r", encoding="utf-8") as plik:
            wyrazy = plik.read().split()

        wyraz = random.choice(wyrazy)    

        print(f"Losowo wybrana liczba z zakresu od {od} do {do} - {liczba}")
        print(f"Losowo wybrany wyraz - {wyraz}")

        with open("out/wynikzadanie.txt", "w", encoding="utf-8") as plik:
            plik.write(f"Losowo wybrana liczba z zakresu od {od} do {do} - {liczba}\n")
            plik.write(f"Losowo wybrany wyraz - {wyraz}")

    except ValueError:
        print("Niepoprawna wartosc")
        
    

main()

