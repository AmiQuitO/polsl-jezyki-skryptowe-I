samogloski = "aąeęioóuy"

ciag = str(input("Podaj ciag znakow: "))

suma = 0

for i in samogloski:
    ile = ciag.count(i)
    if ile != 0:
        suma += ile 
        print(f"{i} - {ile}")

print(f"Ilosc samoglosek: {suma}")
