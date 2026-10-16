lista = []

while True:
    a = input("Podaj element listy: ")
    if a == "":
        break
    lista.append(a)

for i in lista:
    print(i)
