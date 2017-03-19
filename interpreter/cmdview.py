from cmd import Cmd
from view import View
from glob import glob


class CmdView(View, Cmd):
    def __init__(self):
        super(View, self).__init__()
        self.intro = "assignment 1"
        self.prompt = "> "
        self.__controller = None
        print("view initialized")

        # TODO: cmd-line args:
        #   name for welcome message?
        #   -r [filename] to auto read a file?
        #   -d to auto display db

    def set_controller(self, controller):
        self.__controller = controller
        print("controller set")

    def do_quit(self, line):
        """
        Syntax: quit
            Closes the program.

        :param: None
        :return: None
        """
        return True

    def display(self, message):
        print(message)

    def do_read_glob(self, line):
        """
        Syntax: read_glob
            Read files from a directory

        :param: None
        :return: None

        >>> glob('*.txt')
        ['data.txt', 'data2.txt', 'file.txt']
        """

        file_list = glob(line + '*.txt')
        print(file_list)
        for file in file_list:
            with open(file, 'r') as f:
                contents = f.read()
                print(contents)
                self.__controller.load(contents)

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
            self.display("-- No file specified.")
            return
        else:
            with open(line, "r") as file:
                contents = file.read()
                # print(contents)
                self.__controller.load(contents)

    def do_validate(self, line):
        """
        Syntax: validate
            Checks the data to make sure it is valid.

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
        Syntax: get
            Displays data from the database.

        :param: None
        :return: Formatted data
        """
        try:
            stored_data = self.__controller.get_stored()
            print(stored_data)
        except:
            print("failed to query db")

    def do_display(self, flag):
        """
        Syntax: display [flag]
            Displays a chart.

        :param flag: Display different chart types.
            none    Pie chart
            -b      Bar chart
            -l      Line graph
        :return: None
        """
        self.__controller.display(flag)

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

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)