# abstract base class for views
from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    def __init__(self):
        self.__controller = None

    @abstractmethod
    def get(self, line):
        raise NotImplementedError()

    @abstractmethod
    def set(self):
        raise NotImplementedError()

    # @abstractmethod
    # def set_controller(self, controller):
    #     raise NotImplementedError()
    #
    # @abstractmethod
    # def display(self, message):
    #     raise NotImplementedError()
