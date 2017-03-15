class Controller(object):
    def __init__(self, view, parser, validator, db):
        self.__view = view
        self.__parser = parser
        self.__validator = validator
        self.__db = db
        print("controller initialized")

    def load(self, file_contents):
        self.__parser.set_data(file_contents)

    def display(self):
        data = self.__parser.get_data()
        # TODO: implements ways to format data.
        self.__view.display(data)

    def validate(self):
        data = self.__parser.get_data()
        # self.__validator.check(data)
        self.__validator.check_two(data)
        valid_data = self.__validator.get_valid()
        # print(valid_data)

    def get_stored(self):
        employer_data = self.__db.get()
        return employer_data

# TODO: function to query db
# TODO: function to insert to db
