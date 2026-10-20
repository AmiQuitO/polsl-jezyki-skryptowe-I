ciag = str(input("Podaj ciag znakow: "))
jest = True


for i in range(len(ciag)):
    if ciag[i] != ciag[-(i+1)]:
        jest = False
        break

if jest:
    print("Slowo jest palindromem")
else:
    print("Slowo nie jest palindromem")
