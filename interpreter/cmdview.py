from cmd import Cmd
from view import View
from glob import glob
import sys


class CmdView(View, Cmd):
    def __init__(self):
        super(View, self).__init__()
        self.intro = "Interpreter"
        self.prompt = "> "
        self.__controller = None

    def help_cmd(self):
        print(':args:')
        print('\t-g\t\tRead files from cwd')
        print('\t-v\t\tValidate data')
        print('\t-c\t\tCommit valid data to database')
        print('\t-d [data]*\tDisplay default chart (bar chart)')
        print('\t\t\t* up to 3 sets')
        print('\t-r\t\tRebuild the database')

    def _initialise(self):
        print(sys.argv)
        iter_args = iter(sys.argv)
        for arg in sys.argv:
            if arg == '-g':
                self.do_get('')
            elif arg == '-v':
                self.do_validate('')
            elif arg == '-c':
                self.do_commit('')
            elif arg == '-d':
                data_index = sys.argv.index(arg) + 1
                args_list = sys.argv[data_index:]
                formatted_str = ('{} '*len(args_list)).format(*args_list)
                self.do_display('-b ' + formatted_str)
            elif arg == '-r':
                self.do_rebuild_db('')

    def set_controller(self, controller):
        self.__controller = controller
        self._initialise()

    def do_quit(self, line):
        """
        Syntax: quit
            Closes the program.

        :param: None
        :return: None
        """
        return True

    # depricated - moved to fileview
    def do_read_glob(self, line):
        """
        Syntax: read_glob
            Read files from a directory

        :param: None
        :return: None

        >>> glob('*.txt')
        ['data.txt', 'data2.txt', 'data3.txt', 'file.txt']
        """

        file_list = glob(line + '*.txt')
        print(file_list)
        for file in file_list:
            with open(file, 'r') as f:
                contents = f.read()
                print(contents)
                self.__controller.load(contents)

    # depricated
    def do_read(self, line):
        """
        Syntax: read [file-path]
            Reads and processes the contents of a .txt file.

        :param line: A String that represents the path and name of a file to be read.
        :return: None
        """
        # TODO: implement parameter options:
        # -v to auto validate (or verbose?)
        # -c to clean?
        # lines = line.split()
        # if lines.size() > ..etc
        if not line:
            self.display("* No file specified.")
            return
        else:
            with open(line, "r") as file:
                contents = file.read()
                # print(contents)
                self.__controller.load(contents)

    def do_validate(self, line):
        """
        Syntax: validate
            Checks the validity of previously read data before committing it to the database.

        :param: None
        :return: None
        """
        self.__controller.validate()

    def do_commit(self, line):
        """
        Syntax: commit
            Commits valid data to the database to be stored.

        :param: None
        :return: None
        """
        self.__controller.commit()

    def do_get(self, line):
        """
        Syntax: get [dir]
            Reads and processes data from .txt file(s).

        :param [dir]: Optional
            none        If no command is specified, then files in the cwd are read.
            cwd         Shows the current working directory, and lists sub-folders.
            <folder>    Changes the cwd to the specified sub-folder, and reads any .txt files.
        """
        try:
            self.get(line)
        except Exception as e:
            # print("failed to query db")
            print(e)

    def get(self, line):
        self.__controller.get(line)

    def set(self):
        # TODO: print data to console as a table?
        pass

    def do_display(self, line):
        """
        Syntax: display [flag] [data] [data] .. (up to 3)
            Displays a chart comparing data sets.

        :param [flag]: Display chart/graph type.
            -p      Pie chart
            -b      Bar chart
            -l      Line graph
            -r      Radar chart
        :param [data]: Data set to be displayed.
            empid       Unique identifier for employee
            gender      Gender of employee
            age         Age of employee
            salary      Salary of employee
            sales       Sales of employee
            bmi         Body Mass Index of employee
            birthday    Birthday of employee
        """
        self.__controller.display(line)

    # TODO: unfinished?
    def do_query(self, line):
        """
        Syntax: query [key]
            Returns relevant data from the database.

        :param line:
            *   Retrieves all data
            id
            age
            gender
            salary
            bmi
            birthday
        :return:
        """
        self.__controller.query(line)

    def do_rebuild_db(self, line):
        self.__controller.rebuild_db()

    def do_serialize(self, line):
        self.__controller.serialize(line)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)