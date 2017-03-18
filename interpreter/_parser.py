class _Parser(object):
    def __init__(self):
        self.__data = []
        print("parser initialized")

    def set_data(self, data):
        self.__data = data
        print(self.__data)

    def get_data(self):
        return str(self.__data)
