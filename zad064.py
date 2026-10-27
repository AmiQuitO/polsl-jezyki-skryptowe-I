samogloski = "aeiou"

ciag = str(input("Podaj ciag znakow: "))



for i in samogloski:
    print(f"{i} - {ciag.count(i)}")

