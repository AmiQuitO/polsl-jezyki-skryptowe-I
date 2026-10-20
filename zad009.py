lista = [1,"a",True]
lista.append([1,2,3])
lista.append(5j)
lista.append(None)


lista2 = [1,"a",True]
lista2.append([1,2,3])
lista2.append(5j)
lista2.append(None)

print(lista == lista2)
