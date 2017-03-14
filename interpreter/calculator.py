# TODO: change class name.

class Calculator(object):
    def __init__(self):
        self.__data = []
        print("calculator initialized")

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return str(self.__data)