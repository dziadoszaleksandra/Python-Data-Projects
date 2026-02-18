import math
from abc import ABC, abstractmethod

from ..personnel.driver import Driver
from ..personnel.employee import Employee
from .ambulance import Ambulance


class BaseStation(ABC):
    @abstractmethod
    def is_ambulance_available(self):
        pass

    @abstractmethod
    def get_station_info(self):
        pass


class Station(BaseStation):
    __max_id = 0

    def __init__(
        self, location: tuple, ambulance: Ambulance, driver: Driver, employee: Employee
    ):
        self.id = self.get_next_id()
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    @classmethod
    def reset_id_counter(cls):
        cls.__max_id = 0

    def is_ambulance_at_station(self):
        return self.ambulance.location == self.location

    @staticmethod
    def calculate_distance(loc1, loc2):
        return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    def is_ambulance_available(self):
        return self.is_ambulance_at_station() and self.ambulance.status == "available"

    def get_station_info(self):
        return f"Station {self.id}: Location {self.location}, Ambulance {self.ambulance.id}, Driver {self.driver.employee_id}, Employee {self.employee.employee_id}"
