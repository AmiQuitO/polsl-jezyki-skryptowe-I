lista = [2,"a",True,[1,2,3],2,5j,2,None]

elem = 2
ile = 0

for i in lista:
    if i == elem:
        ile += 1

print(f"Ilosc wystapien - {elem} - wynosi: {ile}")
