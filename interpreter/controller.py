class Controller(object):
    def __init__(self, cmdview, fileview, parser, validator, db, vis):
        self.__cmdview = cmdview
        self.__fileview = fileview
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
                flags = line.split()
                print("flgs: ", flags)
                data = self.__db.query(flags[0])
                clean_data = self.__parser.scrub_db_list(data)
                print("clean: ", clean_data)
                print("col: ", flags[0])
                print("flg: ", flags[1])
                if flags[1] == '-b':
                    self.__vis.display_bar(clean_data)
                elif flags[2] == '-l':
                    self.__vis.display_line()
                else:
                    raise Exception("-- Invalid data and/or flag.")
            else:
                self.__vis.display()
        except Exception as e:
            print(e)

    def validate(self):
        data_sets = self.__parser.get_data()
        for data_set in data_sets:
            self.__validator.validate(data_set)

    def commit(self):
        valid_data = self.__validator.get_all_valid()
        for data_set in valid_data:
            self.__db.insert(data_set)

    # depricated
    def get_stored(self):
        all_data = self.__db.get()
        # TODO: send to Formatter??
        if all_data:
            return all_data
        else:
            return "-- No data currently stored."

    # NEW FILE READING METHOD
    def get(self, line):
        data_sets = self.__fileview.get(line)
        for index, data_set in enumerate(data_sets): # TODO: don't need enumeration?
            self.__parser.parse_raw_data(data_set)

    def query(self, line):
        self.__db.query(line)
