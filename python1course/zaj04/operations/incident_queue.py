from .incident import Incident


class IncidentQueue:
    def __init__(self):
        self.__queue = []

    def __getitem__(self, position):
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.__queue[position] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        if len(self):
            return "\n".join(
                [
                    f"{' ' * (4 * idx)}{incident}"
                    for idx, incident in enumerate(self.__queue)
                ]
            )
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new_queue = IncidentQueue()
            new_queue.__queue = self.__queue[:]
            new_queue.__queue.append(other)
            return new_queue
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new_queue = IncidentQueue()
            new_queue.__queue = [other] + self.__queue[:]
            return new_queue
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
            return self
        return NotImplemented

    def __call__(self, id):
        for incident in self.__queue:
            if incident.id == id:
                return incident
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)
