# Przypisania

dane = (2024, "Python", 3.8)
rok, jezyk, wersja = dane
print("Rok:", rok)
print("Język:", jezyk)
print("Wersja:", wersja)

oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print("Pierwsza ocena:", pierwsza)
print("Środkowe oceny:", srodek)
print("Ostatnia ocena:", ostatnia)

info = ("Jan", "Kowalski", 30, "Polska", "programista")
imie, nazwisko, *_, zawod = info
print("Imię:", imie)
print("Nazwisko:", nazwisko)
print("Zawód:", zawod)

dane = (2024, ["Python", 3.8, ("Stabilna", "Wersja")])
rok, [jezyk, wersja, (opis1, opis2)] = dane
opis = opis1 + " " + opis2
print("Rok:", rok)
print("Język:", jezyk)
print("Wersja:", wersja)
print("Opis:", opis)


# Przypisania z wieloma celami i współdzielone referencje

a = b = [1, 2, 3]
b[0] = "zmieniono"
print("Lista a:", a)
print("Lista b:", b)
print("Obie zmienne wskazują na ten sam obiekt w pamięci.")
print("Listy są obiektami mutowalnymi, można je modyfikować w miejscu.")

c = list(a)
c[0] = "nowa wartość"
print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)
print("Kopia listy tworzy nowy obiekt w pamięci, więc zmiana c nie wpływa na a ani b.")

x = y = 10
y = y + 1
print("x =", x)
print("y =", y)
print("Liczby całkowite są obiektami niemutowalnymi.")
print("Zmiana y tworzy nowy obiekt, więc x pozostaje niezmieniony.")


# Przypisania rozszerzone i współdzielone referencje

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print("K =", K)
print("L =", L)
print("M =", M)
print("N =", N)

print(
    "Operator + tworzy nowy obiekt (K i L przestają wskazywać na ten sam).'K = K + [3, 4]' tworzy nową listę, więc 'L' nie ulega zmianie. "
)
print(
    "Operator += modyfikuje istniejącą listę (M i N nadal wskazują na ten sam obiekt). 'M += [3, 4]' modyfikuje istniejącą listę, więc 'N' też się zmienia (ta sama referencja)"
)
