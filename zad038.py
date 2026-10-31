def srednia_skrajnych(liczby):
    if not liczby:
        raise ValueError("Lista nie może być pusta.")

    return (min(liczby) + max(liczby)) / 2

print(srednia_skrajnych([1,4,6,11,24,55]))
