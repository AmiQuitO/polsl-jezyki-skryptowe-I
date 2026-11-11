from datetime import datetime

def Konwertuj(data: str) -> datetime:
    return datetime.strptime(data, "%d.%m.%Y %H:%M:%S")

if __name__ == "__main__":
    #data = str(input("Podaj date w formacie DD.MM.RRRR GG:MM:SS: "))
        
    try:
        data = "11.11.2026 15:30:33"

        print(Konwertuj(data))

    except ValueError:
        print("Niepoprawna data lub format.\nPrzyklad poprawnego zapisu: 11.11.2026 15:30:33") 

