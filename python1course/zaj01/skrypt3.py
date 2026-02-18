# Pętla for z enumerate()

imiona = ["Ola", "Ala", "Iga", "Ida"]
for indeks, imie in enumerate(imiona):
    print(indeks, ":", imie)


# Instrukcje if

liczba1 = int(input("Podaj liczbę: "))
if liczba1 > 0 and liczba1 % 2 == 0:
    print("Liczba jest dodatnia i parzysta")
elif liczba1 > 0:
    print("Liczba jest dodatnia, ale nieparzysta")
else:
    print("Liczba nie jest dodatnia")

liczba2 = int(input("Podaj kolejną liczbę:"))
if liczba2 != 0:
    print("Liczba jest różna od zera")
else:
    print("Liczba to zero")

owoce = ["jabłko", "banan", "pomarańcza"]
owoc = input("Podaj nazwę owocu: ").lower()

if owoc in owoce:
    print("Owoc jest dostępny")
else:
    print("Brak tego owocu w magazynie")


# Pętla while

suma = 0
licznik = 0
while suma <= 100:
    liczba = float(input("Podaj liczbę: "))
    suma += liczba
    licznik += 1
    print("Aktualna suma:", suma)
print("Końcowa suma:", suma)
