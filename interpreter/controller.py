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

    def display(self, line=None):
        try:
            if line:
                data = self.__db.get()
                flag = line.split()
                if flag[0] == '-b':
                    self.__vis.display_bar(data)
                elif flag[0] == '-l':
                    self.__vis.display_line()
                else:
                    raise Exception("-- Invalid flag.")
            else:
                self.__vis.display()
        except Exception as e:
            print(e)

    def validate(self):
        data = self.__parser.get_data()
        self.__validator.check_dict(data)
        # valid_data = self.__validator.get_valid()

    def commit(self):
        valid_data = self.__validator.get_valid()
        self.__db.insert(valid_data)

    def get_stored(self):
        all_data = self.__db.get()
        # TODO: send to Formatter??
        if all_data:
            return all_data
        else:
            return "-- No data currently stored."

    def query(self, line):
        self.__db.query(line)
