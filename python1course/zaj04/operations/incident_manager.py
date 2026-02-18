from ..fleet.station import Station
from .incident import Incident
from .incident_queue import IncidentQueue


class IncidentManager:
    def __init__(self, stations: list):
        self.incidents = IncidentQueue()
        self.stations = stations

    def add_incident(self, incident: Incident):
        self.incidents += incident

    def assign_ambulance(self, incident: Incident):
        available = self.get_available_ambulances()
        if not available:
            return
        available.sort(
            key=lambda a: Station.calculate_distance(a.location, incident.location)
        )
        ambulance = available[0]
        ambulance.status = "at_incident"
        incident.update_status("assigned")

    @staticmethod
    def calculate_priority_score(incident: Incident):
        priority_map = {"low": 1, "medium": 2, "high": 3, "critical": 4}
        return priority_map.get(incident.priority, 0) * (
            incident.get_age_in_minutes() + 1
        )

    def get_available_ambulances(self):
        ambulances = []
        for station in self.stations:
            if station.is_ambulance_available():
                ambulances.append(station.ambulance)
        return ambulances

    def get_incidents_by_status(self, status):
        return [i for i in self.incidents if i.status == status]

    def get_statistics(self):
        total = len(self.incidents)
        if total == 0:
            return {"total_incidents": 0, "avg_response_time": 0}
        total_minutes = sum(
            incident.get_age_in_minutes() for incident in self.incidents
        )
        avg_time = total_minutes / total
        return {"total_incidents": total, "avg_response_time": avg_time}
