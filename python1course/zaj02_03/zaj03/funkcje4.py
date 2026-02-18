# Zadanie 3


def polynomial_calculator(x, *args, **kwargs):
    precyzja = kwargs.get("precyzja", 2)
    dziedzina = kwargs.get("dziedzina")

    if dziedzina is not None:
        if "min" in dziedzina and x < dziedzina["min"]:
            print(
                f"Ostrzeżenie: x = {x} jest mniejsze niż min wartość dziedziny ({dziedzina['min']})"
            )
        if "max" in dziedzina and x > dziedzina["max"]:
            print(
                f"Ostrzeżenie: x = {x} jest większe niż maks wartość dziedziny ({dziedzina['max']})"
            )

    wynik = 0
    stopien = len(args) - 1
    for wsp in args:
        wynik += wsp * (x**stopien)
        stopien -= 1

    return round(wynik, precyzja)


print("\nKalkulator wielomianów")
print(polynomial_calculator(2, 2, 3, 1, 1))
print(polynomial_calculator(5, 1, -2, 3, precyzja=3, dziedzina={"min": 0, "max": 4}))
