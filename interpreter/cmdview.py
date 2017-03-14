from cmd import Cmd
from view import View


class CmdView(View, Cmd):
    def __init__(self):
        super(View, self).__init__()
        self.intro = "assignment 1"
        self.prompt = "> "
        print("view initialized")

    def set_controller(self, controller):
        self.__con = controller
        print("controller set")

    def do_quit(self, line):
        return True

    def display(self, message):
        print(message)

    def do_read(self, line):
        """
        Syntax: read [filepath]
            Reads and processes the contents of a .txt file

        :param line: A String that represents the path and name of a file to be read
        :return: None
        """
        if not line:
            self.display("-- No file specified.")
            return
        else:
            # try:
            #     if line[-3:] ==".txt":
            with open(line, "r") as file:
                contents = file.read()
                print(contents)
                self.__con.load(contents)
            # except:
            #     self.display("-- Wrong file type or file does not exist: Expected .txt")
        #return contents


    def do_get(self, line):
        """
        Syntax: get
            Returns the data previously stored

        :return: Formatted data
        """
        stored_data = self.__con.display()
        return stored_data
