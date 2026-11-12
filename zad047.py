from datetime import datetime

try:
    rok = int(input("Podaj rok: "))
    tydzien = int(input("Podaj tydzien: "))

    kiedy = datetime.fromisocalendar(rok, tydzien, 1)

    print(kiedy.ctime())
except ValueError:
    print("Niepoprawny rok lub numer tygodnia. Podaj poprawne liczby calkowite.")
