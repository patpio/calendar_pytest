from src.event import Event


class Meeting(Event):
    def __init__(self, title, start_time, duration, owner, participants, labels):
        super().__init__(title, start_time, duration, owner, participants)
        self.labels = labels