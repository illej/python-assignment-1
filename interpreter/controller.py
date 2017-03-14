class Controller(object):
    def __init__(self, view, calc):
        self.__view = view
        self.__calc = calc
        print("controller initialized")

    def load(self, file_contents):
        self.__calc.set_data(file_contents)

    def display(self):
        data = self.__calc.get_data()
        # TODO: implements ways to format data.
        self.__view.display("data from calc: " + data)