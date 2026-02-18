# Zadanie 2

imiona = ["Anna", "Jan", "Ewa", "Piotr"]
oceny = [5, 4, 3, 5]

lista_slownikow = [{"imie": imie, "ocena": ocena} for imie, ocena in zip(imiona, oceny)]
print(lista_slownikow)
