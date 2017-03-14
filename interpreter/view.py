# abstract base class for views
from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    def __init__(self):
        self.__con = None

    @abstractmethod
    def set_controller(self, controller):
        raise NotImplementedError()

    @abstractmethod
    def display(self, message):
        raise NotImplementedError()
