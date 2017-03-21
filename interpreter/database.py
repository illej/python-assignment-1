import sqlite3


class Database(object):
    def __init__(self, db):
        self.__db = db
        self.__connection = None # sqlite3.connect(self.__db)
        self.__cursor = None # self.__connection.cursor()
        self.initialise()

    def initialise(self):
        try:
            self.__connection = sqlite3.connect(self.__db)
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(e)
        else:
            print("-- opened database successfully")
        finally:
            print("-- db connection established")

    def rebuild(self):
        try:
            # create table
            self.__cursor.execute('''drop table if exists employee''')
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS employee
                                 (id char(4) PRIMARY KEY NOT NULL,
                                 gender char(1),
                                 age INT(2),
                                 sales INT,
                                 bmi VARCHAR(11),
                                 salary INT,
                                 birthday DATE )''')
            self.__connection.commit()
            print('-- db dropped')
            print('-- db rebuit')
        except Exception as e:
            print(e)

    def insert(self, data_list):
        try:
            sql = "INSERT INTO employee (" \
                  "'id'," \
                  "'gender'," \
                  "'age'," \
                  "'sales'," \
                  "'bmi'," \
                  "'salary'," \
                  "'birthday')" \
                  "VALUES (" \
                  "'{empid}'," \
                  "'{gender}'," \
                  "'{age}'," \
                  "'{sales}'," \
                  "'{bmi}'," \
                  "'{salary}'," \
                  "'{birthday}')".format(**data_list)
            self.__cursor.execute(sql)
            self.__connection.commit()
        except Exception as e:
            print(e)

    # TODO: depricated - if change query -> get and insert -> set, can then inherit View!!!!
    def get(self):
        all_rows = []
        try:
            for row in self.__cursor.execute('SELECT * FROM employee'):
                all_rows.append(row)
            return all_rows
        except Exception as e:
            print(e)

    def query(self, column):
        all_rows = []
        try:
            sql = "select {} from employee".format(column)
            for row in self.__cursor.execute(sql):
                # print("row: ", row)
                all_rows.append(row)
            # print("query result: ", all_rows)
            return all_rows
        except Exception as e:
            print(e)