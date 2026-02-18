# Zadanie 2

import random

liczba = random.randint(1, 100)
proba = 0

print("Zgadnij liczbę od 1 do 100")

while True:
    odpowiedz = int(input("Podaj liczbę:"))
    proba += 1

    if odpowiedz < liczba:
        print("Za mało!")
    elif odpowiedz > liczba:
        print("Za dużo!")
    else:
        print(f"Udało się! Trafiłeś w {proba} próbach.")
        break
