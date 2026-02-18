import pytest
from python1course.zaj06.cinema import CinemaHall, InvalidCancellationError


def test_full_reservation_workflow():
    hall = CinemaHall(rows=2, seats_per_row=2)

    hall.reserve("A1", "Jan")
    hall.cancel("A1", "Jan")
    hall.reserve("A1", "Anna")

    assert hall.get_reservation("A1") == "Anna"


def test_wrong_cancellation_in_workflow():
    hall = CinemaHall()
    hall.reserve("A1", "Jan")

    with pytest.raises(InvalidCancellationError):
        hall.cancel("A1", "Anna")
