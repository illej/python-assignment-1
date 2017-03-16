import sqlite3


class Database(object):
    def __init__(self, db):
        self.__db = db
        self.__connection = None # sqlite3.connect(self.__db)
        self.__conn = None # self.__connection.cursor()
        self.initialise()

        # create table
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS employer
                     (id char(4) PRIMARY KEY NOT NULL, gender char(1), age INT(2), sales INT, bmi VARCHAR(11), salary INT, birthday DATE )''')

        # insert data
        self.__conn.execute("INSERT INTO employer VALUES ('A123','M','32',100,'Normal', 104, '1996-10-24')")

    def initialise(self):
        try:
            self.__connection = sqlite3.connect(self.__db)
        except Exception as e:
            print(e)
        else:
            print("-- opened database successfully")
        finally:
            self.__conn = self.__connection.cursor()
            print("-- db connection established")

    def get(self):
        try:
            for row in self.__conn.execute('SELECT * FROM employer'):
                return row
        except Exception as e:
            print(e)