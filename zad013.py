tekst = str(input("Podaj ciag liter: ")).lower()
samogloski = "aąeęioóuy"

for s in samogloski:
    ile = tekst.count(s)

    if ile > 0:
        print(f"{s} wystepuje {ile} razy w {tekst}")
