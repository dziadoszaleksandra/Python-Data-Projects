from python1course.zaj06.cinema import (
    CinemaHall,
    InvalidCancellationError,
    NoFreeSeatsError,
    SeatOccupiedError,
    UserAlreadyHasReservationError,
)
from python1course.zaj06.dekorator import zmierz_czas


@zmierz_czas(unit="seconds")
def testowa_funkcja(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma


class CinemaWithTimer(CinemaHall):
    @zmierz_czas(unit="microseconds")
    def reserve(self, seat=None, user=None):
        return super().reserve(seat, user)

    @zmierz_czas(unit="microseconds")
    def cancel(self, seat, user):
        return super().cancel(seat, user)


def main():
    print(testowa_funkcja(1000000))

    sala = CinemaWithTimer(rows=3, seats_per_row=4)

    while True:
        print("\n--- Kino ---")
        sala.show_seating()
        print("Opcje: [1] Rezerwuj, [2] Anuluj, [3] Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            user = input("Podaj imię i nazwisko: ")
            seat = input("Podaj miejsce (np. A1) lub pozostaw puste: ").upper()
            seat = seat if seat else None
            try:
                sala.reserve(seat, user)
            except (
                NoFreeSeatsError,
                SeatOccupiedError,
                UserAlreadyHasReservationError,
                ValueError,
            ) as e:
                print(f"Błąd rezerwacji: {e}")

        elif choice == "2":
            user = input("Podaj imię i nazwisko: ")
            seat = input("Podaj miejsce do anulowania (np. A1): ").upper()
            try:
                sala.cancel(seat, user)
            except (InvalidCancellationError, ValueError) as e:
                print(f"Błąd anulowania: {e}")

        elif choice == "3":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()
