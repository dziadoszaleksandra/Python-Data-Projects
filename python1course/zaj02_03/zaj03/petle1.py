# Zadanie 1

imiona = ["Anna", "Jan", "Ewa"]
oceny = [5, 4, 3]

for imie, ocena in zip(imiona, oceny):
    print(f"{imie} ma ocenę {ocena}")

# Jeśli listy mają różne długości to zip ignorując nadmiarowe elementy zatrzyma się na najkrótszej liście
