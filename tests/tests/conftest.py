import pytest
from python1course.zaj06.cinema import CinemaHall


@pytest.fixture
def cinema_hall():
    hall = CinemaHall(rows=5, seats_per_row=5)
    hall.reserve("A1", "Jan")
    hall.reserve("A2", "Anna")
    return hall
