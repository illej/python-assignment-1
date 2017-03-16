from cmd import Cmd
from view import View


class CmdView(View, Cmd):
    def __init__(self):
        super(View, self).__init__()
        self.intro = "assignment 1"
        self.prompt = "> "
        print("view initialized")

        # TODO: cmd-line args:
        #   name for welcome message?
        #   -r [filename] to auto read a file?
        #   -d to auto display db

    def set_controller(self, controller):
        self.__con = controller
        print("controller set")

    def do_quit(self, line):
        return True

    def display(self, message):
        print(message)

    def do_read(self, line):
        """
        Syntax: read [file-path]
            Reads and processes the contents of a .txt file

        :param line: A String that represents the path and name of a file to be read
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
                print(contents)
                self.__con.load(contents)

    def do_validate(self, line):
        self.__con.validate()

    def do_get(self, line):
        """
        Syntax: get
            Returns the previously stored data

        :return: Formatted data
        """
        try:
            stored_data = self.__con.get_stored()
            print(stored_data)
        except:
            print("failed to query db")

    def do_display(self, line):
        self.__con.display()

# TODO: do_function to insert & query db

