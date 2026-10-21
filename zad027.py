with open("in/tekstwejsciowy.txt", "r", encoding="utf-8") as plik:
    tekst = plik.read().lower()

znaki = str(input("Podaj znaki ktore maja byc zliczane np. aeio... : ")).lower()

for z in znaki:
    ile = tekst.count(z)
    print(f"Wystapienia {z.upper()} w tekscie - {ile}")
