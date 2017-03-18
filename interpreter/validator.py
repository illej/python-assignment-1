# receive data
# check library of regex matches
# store any multiple matches in array (named / labeled?)
# return array
import re


class Validator(object):
    def __init__(self):
        self.__regex_lib = {"empid": "[A-Z][0-9]{3}",
                            "gender": "(M|F)",
                            "age": "[0-9]{2}",
                            "sales": "[0-9]{3}",
                            "bmi": "(Normal|Overweight|Obesity|Underweight)",
                            "salary": "[0-9]{2,3}",
                            "birthday": "[1-31]{2}-[1-12]{2}-[0-9]{4}"}
        self.__valid_dict = {}

    def get_valid(self):
        """
        >>> Validator().get_valid()
        -- No valid data has been entered.
        """
        try:
            if self.__valid_dict:
                return self.__valid_dict
            else:
                raise Exception('-- No valid data has been entered.')
        except Exception as e:
            print(e)

    def check_dict(self, file_contents):
        """
        >>> "empid=1234\\nage=24".split()
        ['empid=1234', 'age=24']
        >>> file_dict = dict(pair.split('=') for pair in ['empid=D011', 'age=20'])
        >>> file_dict['empid']
        'D011'
        """
        file_lines = file_contents.split() # ['empid=D011', ..]
        file_dict = dict(pair.split('=') for pair in file_lines) # {'empid': 'D011'}
        for key, value in file_dict.items():
            try:
                match = re.search(self.__regex_lib[key], value)
                if match:
                    self.__valid_dict[key] = value
                else:
                    raise Exception('-- Invalid data: ' + key + ' = ' + value)
            except Exception as e:
                print(e)

        if len(self.__valid_dict) != len(self.__regex_lib):
            self.__valid_dict = {}
            print('-- Data invaild. Enter new data.')
        else:
            print('* Data validation successful.')

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)