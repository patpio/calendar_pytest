from abc import ABCMeta, abstractmethod


class EventAbc(metaclass=ABCMeta):
    @property
    @abstractmethod
    def duration(self):
        pass

    @duration.setter
    @abstractmethod
    def duration(self, value):
        pass

    @property
    @abstractmethod
    def start_time(self):
        pass

    @start_time.setter
    @abstractmethod
    def start_time(self, value):
        pass