from src.event import Event


class Workshop(Event):
    def __init__(self, title, start_time, duration, owner, participants, location):
        super().__init__(title, start_time, duration, owner, participants)
        self.location = location