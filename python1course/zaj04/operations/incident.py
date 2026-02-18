from datetime import datetime


class Incident:
    __slots__ = (
        "description",
        "id",
        "location",
        "priority",
        "reported_at",
        "reporter_name",
        "reporter_phone",
        "status",
    )
    __max_id = 0

    PRIORITIES = {"low", "medium", "high", "critical"}
    STATUSES = {"reported", "assigned", "in_progress", "resolved"}

    def __init__(
        self,
        description,
        priority="low",
        reporter_name="",
        reporter_phone="",
        location=(0, 0),
    ):
        self.id = self.get_next_id()
        self.description = description
        self.priority = priority if self.validate_priority(priority) else "low"
        self.reporter_name = reporter_name
        self.reporter_phone = reporter_phone
        self.status = "reported"
        self.reported_at = datetime.now()
        self.location = location

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    @classmethod
    def reset_id_counter(cls):
        cls.__max_id = 0

    @staticmethod
    def validate_priority(priority):
        return priority in Incident.PRIORITIES

    def get_age_in_minutes(self):
        delta = datetime.now() - self.reported_at
        return int(delta.total_seconds() / 60)

    def update_status(self, new_status):
        if new_status in self.STATUSES:
            self.status = new_status

    def __str__(self):
        return (
            f"Incident {self.id}: {self.description}, Priority: {self.priority}, "
            f"Status: {self.status}, Reporter: {self.reporter_name}, "
            f"Phone: {self.reporter_phone}, Location: {self.location}"
        )

    def __repr__(self):
        return (
            f"Incident('{self.description}', priority='{self.priority}', "
            f"reporter_name='{self.reporter_name}', reporter_phone='{self.reporter_phone}', "
            f"location={self.location})"
        )
