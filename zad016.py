import math

liczby = []

with open("in/zad016txt.txt", "r", encoding="utf-8") as dane:
    plik = dane.read()
    elementy = plik.split()
    liczby = [int(element) for element in elementy] 

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
