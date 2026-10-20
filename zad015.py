import math

liczby = []

while True:
    l = input("Podaj liczbe: ")
    if l == "":
        break
    liczby.append(int(l))

suma = 0
srednia = 0
mediana = 0

for i in liczby:
    suma += i

srednia = suma / len(liczby)

if len(liczby)%2==0:
    mediana = (liczby[math.floor(len(liczby)/2) - 1] + liczby[math.ceil(len(liczby)/2)]) / 2
else:
    mediana = liczby[math.floor(len(liczby)/2)]

print(liczby)
print(f"Suma wynosi: {suma} --- Srednia wynosi: {srednia} --- Mediana wynosi: {mediana}")
