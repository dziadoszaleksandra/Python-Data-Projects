# Zadanie 1


def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc = cena * ilosc
    tekst = (
        f"Zamówienie: {nazwa_produktu}, ilość: {ilosc}, łączna cena: {wartosc:.2f} zł"
    )
    return tekst, wartosc


zamowienia = []
zamowienia.append(zamowienie_produktu("Jabłka", cena=3.5, ilosc=4))
zamowienia.append(zamowienie_produktu("Banany", cena=5.0, ilosc=2))
zamowienia.append(zamowienie_produktu("Mleko", cena=4.2))

print("\n Lista zamówień: ")
suma = 0
for tekst, wartosc in zamowienia:
    print(tekst)
    suma += wartosc

print(f"\n Łączna wartość wszystkich zamówień: {suma:.2f} zł")
