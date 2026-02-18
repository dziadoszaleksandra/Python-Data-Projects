# python1course/zaj04/__init__.py

# Importujemy konkretne klasy z podkatalogów, aby były dostępne bezpośrednio w pakiecie zaj04

# Z katalogu fleet
from .fleet.ambulance import Ambulance
from .fleet.station import Station
from .operations.incident import Incident

# Z katalogu operations
from .operations.incident_manager import IncidentManager

# Z katalogu personnel
from .personnel.driver import Driver
from .personnel.employee import Employee

# Definiujemy co jest widoczne na zewnątrz
__all__ = ["Ambulance", "Driver", "Employee", "Incident", "IncidentManager", "Station"]
