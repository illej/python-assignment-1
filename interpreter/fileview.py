from view import View
from glob import glob


class FileView(View):
    def __init__(self):
        super(View, self).__init__()

    def set_controller(self, controller):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def display(self, **kwargs):
        pass

    def get(self, line):
        """
        Syntax: read_glob
            Read files from a directory

        :param: None
        :return: None

        >>> glob('*.txt')
        ['data.txt', 'data2.txt', 'data3.txt', 'file.txt']
        >>> raw_file = FileView().get('*.txt')
        >>> raw_file[0]
        'empid=D011\\ngender=m\\nage=29\\nsales=722\\nbmi=normal\\nsalary=320\\nbirthday=23-11-1987'
        """
        raw_file_list = []
        filename_list = glob('*.txt')
        for file in filename_list:
            with open(file, 'r') as f:
                contents = f.read()
                data_sets = contents.split("\n\n")
                for data_set in data_sets:
                    raw_file_list.append(data_set)
                    # print(raw_file_list)


                # self.__controller.load(contents)
        return raw_file_list

        # CURRENT WORKING DO_READ
        # if not line:
        #     self.display("-- No file specified.")
        #     return
        # else:
        #     with open(line, "r") as file:
        #         contents = file.read()
        #         # print(contents)
        #         self.__controller.load(contents)

    def set(self):
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()