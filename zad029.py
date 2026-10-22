with open("in/tekstdostatystyki.txt", "r", encoding="utf-8") as plik:
    tekst = plik.read().lower()

czysty_tekst = ""

for i in tekst:
    if not i.isalpha():
        czysty_tekst += " "
        continue
    czysty_tekst += i

wyrazy = czysty_tekst.split()

statystyka = {}

for wyraz in wyrazy:
    if wyraz in statystyka:
        statystyka[wyraz] += 1
    else:
        statystyka[wyraz] = 1

print(f"Liczba wyrazow - {len(wyrazy)}")
print(f"Liczba roznych wyrazow - {len(statystyka)}")
print("Liczba wystapien poszczegolnych wyrazow: ")

for w in sorted(statystyka):
    print(f"{w} - {statystyka[w]}")
