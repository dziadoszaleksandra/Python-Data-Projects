import math
import random

# działania matematyczne
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12
tekst = str(potega)
wartosc_pi = math.pi
losowa = random.choice([1, 2, 3, 4, 5])


# łańcuchy znaków
print(tekst)
tekst = f"Wartosc: {tekst}"
print("Długość tekstu:", len(tekst))
print("Fragment zawierający 'art':", tekst[1:4])
print("Dir:", dir(tekst))
print("Wielkie litery :", tekst.upper())
# próba zmiany znaku =bląd
# tekst[2] = 'p'  # TypeError: 'str' object does not support item assignment
# Zamiast modyfikować string, trzeba stworzyć nowy
nowy = tekst[:2] + "p" + tekst[3:]
print("nowy tekst = ", nowy)


# listy
lista = list(tekst)
lista = [c.upper() for c in lista[:7]] + [":"]
print("Lista po wycinku i uppercase + ':' =", lista)
lista.append([1, 2, 3, 4, 5])
print("Lista po dodaniu [1,2,3,4,5]:", lista)
if ":" in lista:
    lista.remove(":")
print("Lista po usunięciu dwukropka:", lista)

# listy składane
lista2 = [1, 2, 3, "banan", 100]
lista3 = [x**2 for x in lista2 if x != "banan"]
lista4 = [x for x in range(2, 17, 2)]
print("lista2:", lista2)
print("lista3:", lista3)
print("lista4:", lista4)


# słowniki
ja = {}
ja["imie"] = "Aleksandra"
ja["nazwisko"] = "Dziadosz"
ja["wiek"] = 19
ja["moje_hobby"] = [
    {"nazwa": "bieganie", "dlaczego": "bo to zdrowe"},
    {
        "nazwa": "podróże",
        "dlaczego": "pozawala mi odkrywać nowe kultury i nowych ludzi",
    },
]
print("moje_hobby:", ja["moje_hobby"])
print("Pierwsze hobby:", ja["moje_hobby"][0]["nazwa"])
print("Klucze słownika:", ja.keys())
print("Czy istnieje klucz 'adres'?", "adres" in ja)


# krotki
krotka1 = (1, 2, "3", 4, 2, 5)
print("Długość krotki:", len(krotka1))
print("Pierwszy element:", krotka1[0])
print("Ile razy występuje 2:", krotka1.count(2))
# próba modyfikacji spowoduje TypeError (nie wykonuje się tego, bo krotki sa niemutowalne)


# zbiory
X = set("kalarepa")
Y = set("lepy")
print("Zbiór X:", X)
print("Zbiór Y:", Y)
print("część wspólna (X & Y):", X & Y)
