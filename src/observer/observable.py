import abc


class Observable(abc.ABC):
    def __init__(self) -> None:
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observer(self, data):
        for observer in self._observers:
            observer.update(data)
