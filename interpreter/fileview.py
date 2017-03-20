from view import View
from glob import glob


class FileView(View):
    def __init__(self):
        super(View, self).__init__()

    def get(self, line):
        """
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
        return raw_file_list

    def set(self):
        # TODO: write data to file?
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()