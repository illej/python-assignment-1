class Controller(object):
    def __init__(self, cmdview, fileview, parser, validator, db, vis):
        self.__cmdview = cmdview
        self.__fileview = fileview
        self.__parser = parser
        self.__validator = validator
        self.__db = db
        self.__vis = vis

    def load(self, file_contents):
        self.__parser.set_data(file_contents)

    def display(self, line=None):
        try:
            if line:
                data_set_dict = {}
                input = line.split()
                # print("input: ", input)
                if len(input) > 1:
                    if input[1] in self.__validator.get_valid_cols():
                        if input[0] in self.__validator.get_valid_flags():
                            iterinput = iter(input)
                            next(iterinput)
                            for set in iterinput:
                                data = self.__db.query(set)
                                clean_data = self.__parser.scrub_db_list(data)
                                data_set_dict[set] = clean_data

                                # print("d-s-ls: ", data_set_dict)
                            if input[0] == '-b':
                                self.__vis.display_bar(data_set_dict)
                            elif input[0] == '-l':
                                self.__vis.display_line(data_set_dict)
                            elif input[0] == '-p':
                                self.__vis.display_pie(data_set_dict)
                            elif input[0] == '-r':
                                self.__vis.display_radar(data_set_dict)
                        else:
                            raise Exception("-- Invalid flag.")
                    else:
                        raise Exception("-- Invalid data.")
                else:
                    raise Exception("* Invalid input. \n-- Type 'help display' for information on how to use this command.")
            else:
                raise Exception("* Missing parameters. \n-- Type 'help display' for information on how to use this command.")
        except Exception as e:
            print(e)

    def validate(self):
        try:
            if self.__parser.get_data():
                data_sets = self.__parser.get_data()
                for data_set in data_sets:
                    self.__validator.validate(data_set)
            else:
                raise Exception("* No data has been read.\n-- Type 'help get' for more details.")
        except Exception as e:
            print(e)

    def commit(self):
        try:
            valid_data = self.__validator.get_valid_sets()
            for data_set in valid_data:
                self.__db.insert(data_set)
        except Exception as e:
            print("* Could not commit data to the database.\n-- Type 'help commit' for more details.")

    def rebuild_db(self):
        self.__db.rebuild()

    # depricated
    def get_stored(self):
        all_data = self.__db.get()
        # TODO: send to Formatter??
        if all_data:
            return all_data
        else:
            return "* No data currently stored."

    # NEW FILE READING METHOD
    def get(self, line):
        data_sets = self.__fileview.get(line)
        for index, data_set in enumerate(data_sets): # TODO: don't need enumeration?
            self.__parser.parse_raw_data(data_set)

    def query(self, line):
        print(self.__db.query(line))

    def serialize(self, line):
        try:
            import pickle
            args = line.split()
            if len(args) == 1 and args[0] != '-r':
                # write
                filename = args[0] + '.pickle'
                db_contents = self.__db.query('*')
                if db_contents:
                    with open(filename, 'wb') as p_file:
                        pickle.dump(db_contents, p_file)
                    print('-- Database pickled!\n\t-> as filename: {}.'.format(filename))
                else:
                    raise Exception('* Database is empty. Nothing to serialize.')
            elif len(args) == 2 and args[0] == '-r':
                # read
                filename = args[1] + '.pickle'
                try:
                    with open(filename, 'rb') as p_file:
                        data = pickle.load(p_file)
                    # TODO: display somehow?
                    # print('comparison with db: ', data == self.__db.query('*'))
                    # output = "\n".join(str(i) for i in data)
                    # print(output)
                    print(data[0])
                except Exception as e:
                    print(e)
            else:
                raise Exception("* Invalid parameters.\n-- Type 'help serialize' for more details.")
        except Exception as e:
            print(e)
