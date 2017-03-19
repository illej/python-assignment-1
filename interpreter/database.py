import sqlite3


class Database(object):
    def __init__(self, db):
        self.__db = db
        self.__connection = None # sqlite3.connect(self.__db)
        self.__cursor = None # self.__connection.cursor()
        self.initialise()

        # create table
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS employee
                     (id char(4) PRIMARY KEY NOT NULL,
                     gender char(1),
                     age INT(2),
                     sales INT,
                     bmi VARCHAR(11),
                     salary INT,
                     birthday DATE )''')

        # insert data
        self.__cursor.execute("INSERT INTO employer VALUES ('A123','M','32',100,'Normal', 104, '1996-10-24')")

    def initialise(self):
        try:
            self.__connection = sqlite3.connect(self.__db)
        except Exception as e:
            print(e)
        else:
            print("-- opened database successfully")
        finally:
            self.__cursor = self.__connection.cursor()
            print("-- db connection established")

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
        except Exception as e:
            print(e)

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
            print(sql)
            for row in self.__cursor.execute(sql):
                all_rows.append(row)
            print(all_rows)
        except Exception as e:
            print(e)