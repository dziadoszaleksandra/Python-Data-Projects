# Zadanie 3

import math

trojkaty = [(3, 4, 5), (5, 12, 13), (7, 8, 9), (8, 15, 17)]

for idx, (a, b, c) in enumerate(trojkaty):
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

    if a**2 + b**2 == c**2:
        print(f"Trójkąt #{idx}: boki = ({a}, {b}, {c})")
        print(f"Pole: {pole:.2f}")
        print("To jest trójkąt prostokątny\n")
