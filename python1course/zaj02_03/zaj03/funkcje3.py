# Zadanie 2


def oblicz_srednia_ocen(*oceny, wagi=None):
    if not oceny:
        return 0

    if wagi is None:
        return sum(oceny) / len(oceny)
    else:
        suma_wazona = 0
        suma_wag = 0
        for ocena in oceny:
            waga = wagi.get(ocena, 1)
            suma_wazona += ocena * waga
            suma_wag += waga
        return suma_wazona / suma_wag


print("\n Średnia zwykła:")
print(oblicz_srednia_ocen(4, 5, 3, 5))

print("\nŚrednia ważona: ")
print(oblicz_srednia_ocen(4, 5, 3, 5, wagi={4: 2, 5: 3, 3: 1}))
