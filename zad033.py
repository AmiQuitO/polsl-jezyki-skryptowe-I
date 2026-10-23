while True:
    try:
        od = int(input("Podaj zakres roku od: "))
        do = int(input("Podaj zakres roku do: "))

        if od < do:
            break
        print("Poczatek zakresu musi byc wiekszy niz jego koniec")
    except ValueError:
        print("Podaj poprawna wartosc")

lata = [x for x in range(od, do+1) if x%400==0 or (x%4==0 and not x%100==0)]

print(f"Lata przystepne w zakresie od {od} do {do}: ")
for i in lata:
    print(i)
