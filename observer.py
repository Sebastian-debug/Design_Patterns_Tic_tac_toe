from abc import abstractmethod


class Subject:
    """
    A class to represent the subject interface for the concrete subject.

    Attributes
    ----------
    Methods
    -------
    attach(observer):
        abstract method for attaching an observer
    detach(observer):
        abstract method for detaching an observer
    notify():
        abstract method for notifying all attached observers

    """
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer:
    """
    A class to represent the observer interface for the concrete observer.

    Attributes
    ----------
    Methods
    -------
    update():
        the update function for the observer

    """
    @abstractmethod
    def update(self):
        pass
