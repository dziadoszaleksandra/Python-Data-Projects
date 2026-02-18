# Zadanie 1


def zmien_wartosc(arg):
    if isinstance(arg, list):
        print(
            "Wewnątrz funkcji: wykryto listę, zmieniam pierwszy element na 'kalafior'"
        )
        arg[0] = "kalafior"
    elif isinstance(arg, int):
        print(
            "Wewnątrz funkcji: wykryto liczbę całkowitą, przypisuję nową wartość 65482652"
        )
        arg = 65482652
    return arg


print(" Lista 1 (niemutowalna)")
liczba = 10
print("Przed funkcją:", liczba)
zmien_wartosc(liczba)
print("Po funkcji:", liczba)

print("\n Lista 2 (mutowalna)")
lista = ["marchew", "ziemniak", "ogórek"]
print("Przed funkcją:", lista)
zmien_wartosc(lista)
print("Po funkcji:", lista)

# Liczby (typ niemutowalny) nie zmieniają się poza funkcją.
# Listy (typ mutowalny) zostają zmodyfikowane także poza funkcją.
