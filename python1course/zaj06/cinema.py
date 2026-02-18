import string
from python1course.zaj07.utils.logging import get_logger

logger = get_logger(__name__)

# --- WYJĄTKI ---


class SeatOccupiedError(Exception):
    pass


class SeatNotFoundError(Exception):
    pass


class InvalidCancellationError(Exception):
    pass


class UserAlreadyHasReservationError(Exception):
    pass


# --- KLASA KINA ---


class CinemaHall:
    def __init__(self, rows=5, seats_per_row=10):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = self._generate_seats()
        logger.debug(f"Utworzono salę kinową ({len(self.seats)} miejsc)")

    def _generate_seats(self):
        seats = {}
        row_letters = string.ascii_uppercase[: self.rows]

        for row in row_letters:
            for num in range(1, self.seats_per_row + 1):
                seat_id = f"{row}{num}"
                seats[seat_id] = None
        return seats

    def get_reservation(self, seat: str):
        """Zwraca osobę, która zarezerwowała miejsce, lub None."""
        if seat not in self.seats:
            raise SeatNotFoundError(f"Miejsce {seat} nie istnieje.")
        return self.seats[seat]

    def reserve(self, seat: str, user: str):
        logger.debug(f"reserve(): seat={seat}, user={user}")

        # 1. Sprawdź czy miejsce istnieje
        if seat not in self.seats:
            logger.error(f"Miejsce {seat} nie istnieje")
            raise SeatNotFoundError(f"Miejsce {seat} nie istnieje.")

        # 2. Sprawdź, czy użytkownik ma już rezerwację
        if user in self.seats.values():
            logger.error(f"Użytkownik {user} ma już rezerwację")
            raise UserAlreadyHasReservationError(
                f"Użytkownik {user} ma już rezerwację."
            )

        # 3. Sprawdź czy miejsce jest zajęte
        if self.seats[seat] is not None:
            logger.warning(f"Miejsce {seat} jest już zajęte")
            raise SeatOccupiedError(f"Miejsce {seat} jest już zajęte.")

        # 4. Rezerwacja
        self.seats[seat] = user
        logger.info(f"Zarezerwowano miejsce {seat} dla {user}")

    def cancel(self, seat: str, customer: str):
        """Metoda nazywa się teraz 'cancel', aby pasowała do testów."""
        logger.debug(f"cancel(): seat={seat}, customer={customer}")

        # 1. Sprawdź czy miejsce istnieje
        if seat not in self.seats:
            logger.error(f"Miejsce {seat} nie istnieje")
            raise SeatNotFoundError(f"Miejsce {seat} nie istnieje.")

        current_booking = self.seats[seat]

        # 2. Sprawdź czy miejsce jest w ogóle zarezerwowane
        if current_booking is None:
            logger.warning(f"Miejsce {seat} nie jest zarezerwowane")
            raise InvalidCancellationError(f"Miejsce {seat} nie jest zarezerwowane.")

        # 3. Sprawdź czy anuluje właściwa osoba
        if current_booking != customer:
            logger.error(
                f"Próba anulowania przez inną osobę: {customer} vs {current_booking}"
            )
            raise InvalidCancellationError("Nie można anulować rezerwacji innej osoby.")

        # 4. Anuluj
        self.seats[seat] = None
        logger.info(f"Anulowano rezerwację miejsca {seat} (użytkownik {customer})")
