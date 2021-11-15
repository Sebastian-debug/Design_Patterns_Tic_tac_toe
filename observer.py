from abc import abstractmethod


class Subject:

    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.discard(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(observer)


class Observer:

    @abstractmethod
    def update(self, subject: Subject):
        pass



