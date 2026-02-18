import time


def zmierz_czas(unit="seconds"):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            start = time.time()
            wynik = funkcja(*args, **kwargs)
            end = time.time()
            czas = end - start
            if unit == "microseconds":
                czas *= 1_000_000
                print(f"Czas wykonania funkcji {funkcja.__name__}: {czas:.2f} µs")
            else:
                print(f"Czas wykonania funkcji {funkcja.__name__}: {czas:.6f} s")
            return wynik

        return wrapper

    return dekorator
