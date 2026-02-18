from os import getcwd

current_path = getcwd()
print("Wartość zmiennej:", current_path)

import czas

print("Aktualny czas:", czas.aktualny_czas)

import time

time.sleep(20)
print("Ponowny aktualny czas:", czas.aktualny_czas)

import importlib

importlib.reload(czas)
print("Czas aktualny po przeładowaniu:", czas.aktualny_czas)
