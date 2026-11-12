from datetime import datetime

teraz = datetime.now()

czas = teraz.strftime("%H : %M : %S")

print(czas)
