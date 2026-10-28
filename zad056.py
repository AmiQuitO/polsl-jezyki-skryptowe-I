import random

lista = [i for i in range(1, 101)]

# 1 wersja
random.shuffle(lista)

print(f"Wersa z random.shuffle():")
for i in lista:
    print(i, end=",")

# 2 wersja
lista = [i for i in range(1, 101)]

for i in range(len(lista)):
    j = random.randint(0, len(lista)-1)
    lista[i], lista[j] = lista[j], lista[i]

print(f"\nWersa z petla i random.randint():")
for i in lista:
    print(i, end=",")
