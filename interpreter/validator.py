# receive data
# check library of regex matches
# store any multiple matches in array (named / labeled?)
# return array
import re


class Validator(object):
    def __init__(self):
        self.__key_lib = ["empid",
                          "gender",
                          "age",
                          "sales",
                          "bmi",
                          "salary",
                          "birthday"]
        self.__value_lib = {"empid": "[A-Z][0-9]{3}",
                            "gender": "(M|F)",
                            "age": "[0-9]{2}",
                            "sales": "[0-9]{3}",
                            "bmi": "(Normal|Overweight|Obesity|Underweight)",
                            "salary": "[0-9]{2,3}",
                            "birthday": "[1-31]{2}-[1-12]{2}-[0-9]{4}"}
        self.__valid = []

    def check(self, file_contents):
        # split file into separate lines
        lines = file_contents.split()
        print(lines)
        # for each line..
        for line in lines:
            # check against a library of keys
            for key in self.__key_lib:
                match = re.search(key, line)
                # if a valid key is found..
                if match:
                    # store the value (assoc regex)
                    value = self.__value_lib[match.group(0)]  # match[0] dereferences the value!
                    # find the value matching the regex
                    data_match = re.search(value, line, flags=re.IGNORECASE)
                    # if a valid value is found..
                    if data_match:
                        # store in a list
                        # TODO: possibly build a dictionary instead
                        self.__valid.append(data_match.group(0))

    def check_two(self, file_contents):
        lines = file_contents.split()
        print(lines)

        data_dict = dict(pair.split('=') for pair in lines)
        print(data_dict)

    def get_valid(self):
        return self.__valid

    # attempt 1
    # for key, value.. in dict
    #     for key2, value2.. in file_dict
    #         if key == key2:
    #             if value == value2:
    #                 return "success!"

    # attempt 2
    # for key, value.. in regex_dict:
    #     value2 = file_dict[key]
    #         if value == value2:
    #             return "success!"

# attempt 3 TODO: use regex instead of of '=='
# TODO: merge parser and validator? what is parser even doing if the db is holding the data????
