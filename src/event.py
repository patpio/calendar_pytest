import datetime

from src.event_abc import EventAbc


class Event(EventAbc):
    def __init__(self, title, start_time, duration, owner, participants):
        self.title = title
        self.start_time = start_time
        self.duration = duration
        self.owner = owner
        self.participants = participants

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if value <= datetime.timedelta(minutes=15):
            raise ValueError(f'Event duration must be over 15 minutes. {value}')
        self._duration = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        if datetime.datetime.now() + datetime.timedelta(minutes=10) > value:
            raise ValueError(f'Event start_time can not start in less than 10 minutes. {value} ')
        self._start_time = value

    def __str__(self):
        return f'Event {self.title} starts at {self.start_time}.'

    def __repr__(self):
        return f'{type(self).__name__}(title="{self.title}", start_time={repr(self.start_time)}, ' \
               f'duration={self.duration!r}, owner="{self.owner}", participants={self.participants})'
