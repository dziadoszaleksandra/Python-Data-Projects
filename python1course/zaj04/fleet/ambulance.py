class Ambulance:
    __max_id = 0
    STATUSES = {"available", "busy", "at_incident"}

    def __init__(self, status="available", location=(0, 0)):
        self.id = self.get_next_id()
        self.status = status
        self.location = location

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    @classmethod
    def reset_id_counter(cls):
        cls.__max_id = 0
