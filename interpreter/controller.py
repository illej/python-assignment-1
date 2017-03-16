class Controller(object):
    def __init__(self, view, parser, validator, db, vis):
        self.__view = view
        self.__parser = parser
        self.__validator = validator
        self.__db = db
        self.__vis = vis
        print("controller initialized")

    def load(self, file_contents):
        self.__parser.set_data(file_contents)

    def display(self, flag=None):
        if flag == '-b':
            self.__vis.display_bar()
        elif flag == '-l':
            self.__vis.display_line()
        else:
            self.__vis.display()

    def validate(self):
        data = self.__parser.get_data()
        self.__validator.check_dict(data)
        # valid_data = self.__validator.get_valid()

    def commit(self):
        valid_data = self.__validator.get_valid()
        self.__db.insert(valid_data)

    def get_stored(self):
        employer_data = self.__db.get()
        return employer_data
