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
        self.__valid_dicts_list = []
        self.__valid_dict = {}

    def get_all_valid(self):
        try:
            if self.__valid_dicts_list:
                return self.__valid_dicts_list
            else:
                raise Exception('-- No valid data has been entered.')
        except Exception as e:
            print(e)

    def validate(self, file_contents):
        """
        >>> "empid=1234\\nage=24".split()
        ['empid=1234', 'age=24']
        >>> file_dict = dict(pair.split('=') for pair in ['empid=D011', 'age=20'])
        >>> file_dict['empid']
        'D011'
        """
        valid_dict = {}
        for key, value in file_contents.items(): # file_dict
            try:
                match = re.search(self.__regex_lib[key], value)
                if match:
                    valid_dict[key] = value
                else:
                    raise Exception('-- Invalid data: ' + key + ' = ' + value)
            except Exception as e:
                print(e)

        if len(valid_dict) != len(self.__regex_lib):
            valid_dict.clear()
            print('-- Data invaild. Enter new data.')
        else:
            print('* Data validation successful.')
            self.__valid_dicts_list.append(valid_dict)
            print("val.state of valid_dicts: ", self.__valid_dicts_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
