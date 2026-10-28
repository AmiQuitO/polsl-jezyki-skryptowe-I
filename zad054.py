dziesietny = float(input("Podaj liczbe dodatnia w zapisie dziesietnym np 0.5: "))

licznik = 1
mianownik = 1

while True:
    ulamek = licznik/mianownik
    if dziesietny > ulamek:
        licznik += 1
    elif dziesietny < ulamek:
        mianownik += 1
    else:
        break

print(f"{dziesietny} wynosi {licznik}/{mianownik}")
