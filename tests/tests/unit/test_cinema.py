import pytest
from python1course.zaj06.cinema import (
    CinemaHall,
    InvalidCancellationError,
    UserAlreadyHasReservationError,
    SeatNotFoundError,
    SeatOccupiedError,
)


def test_reserve_seat():
    hall = CinemaHall()
    hall.reserve("A1", "Jan")
    assert hall.get_reservation("A1") == "Jan"


def test_user_already_has_reservation():
    hall = CinemaHall()
    hall.reserve("A1", "Jan")
    with pytest.raises(UserAlreadyHasReservationError):
        hall.reserve("A2", "Jan")


def test_cancel_reservation():
    hall = CinemaHall()
    hall.reserve("A1", "Jan")
    hall.cancel("A1", "Jan")
    assert hall.get_reservation("A1") is None


def test_cancel_wrong_user():
    hall = CinemaHall()
    hall.reserve("A1", "Jan")
    with pytest.raises(InvalidCancellationError):
        hall.cancel("A1", "Anna")


@pytest.mark.parametrize(
    "seat,user,exception",
    [
        # A1 jest zajęte przez Piotra (w setupie poniżej), więc Jan rezerwuje B1 (sukces)
        ("B1", "Jan", None),
        # Anna próbuje zająć A1, które ma Piotr -> Oczekujemy błędu SeatOccupiedError
        ("A1", "Anna", SeatOccupiedError),
        # Jan próbuje zająć nieistniejące miejsce -> Oczekujemy SeatNotFoundError
        ("Z9", "Jan", SeatNotFoundError),
    ],
    ids=["valid_seat", "overwrite_seat", "invalid_seat"],
)
def test_reservation_parametrized(seat, user, exception):
    hall = CinemaHall()
    hall.reserve("A1", "Piotr")  # Warunek wstępny: Piotr zajmuje A1

    if exception:
        with pytest.raises(exception):
            hall.reserve(seat, user)
    else:
        hall.reserve(seat, user)
