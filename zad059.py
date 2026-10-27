def przelicz(liczba: str):
    rzymskie = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1
            }

    if not liczba:
        raise ValueError("Nie podano liczby. ")
    if any(znak not in rzymskie for znak in liczba):
        raise ValueError("Podano nieznany symbol. ")

    dziesietne = [rzymskie[l] for l in liczba]
    
    print(dziesietne)

    dziesietne_odwrot = dziesietne[::-1]
    suma = 0
    for i in range(len(dziesietne_odwrot)):
        if i > 0 and dziesietne_odwrot[i] < dziesietne_odwrot[i-1]:
            suma -= dziesietne_odwrot[i]
        else:
            suma += dziesietne_odwrot[i]

    return suma


try:
    print(przelicz("IV")) # 4
    print(przelicz("XIV")) # 14 
    print(przelicz("XVI")) # 16
    print(przelicz("IX")) # 9 
    print(przelicz("XL")) # 40
    print(przelicz("XC")) # 90
    print(przelicz("CD")) # 400
    print(przelicz("CM")) # 900
except ValueError as e:
    print(e)
