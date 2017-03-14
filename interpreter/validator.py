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
                            "gender": "(M|F)",  # TODO: .toLowerCase() ??
                            "age": "[0-9]{2}",
                            "sales": "[0-9]{3}",
                            "bmi": "(Normal|Overweight|Obesity|Underweight)",  # TODO: .toLowerCase() ??
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
                    value = self.__value_lib[match[0]]  # match[0] dereferences the value!
                    # find the value matching the regex
                    data_match = re.search(value, line, flags=re.IGNORECASE)
                    # if a valid value is found..
                    if data_match:
                        # store in a list
                        # TODO: possibly build a dictionary instead
                        self.__valid.append(data_match[0])

    def get_valid(self):
        return self.__valid
