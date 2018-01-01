import sqlite3


def create_db(database_path: str):
    conn = sqlite3.connect(database_path)
    ddl = "CREATE TABLE main ( " \
          "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, " \
          "surname       STRING," \
          "first_name    STRING," \
          "patronymic    STRING," \
          "live_place    STRING," \
          "activity_type STRING," \
          "state         STRING);"
    conn.cursor().execute(ddl)
    conn.close()



def save_to_db(dct: dict, database_path: str):
    conn = sqlite3.connect(database_path)


def find_by_name():
    # TODO: find record in db by name
    pass


def clear_db(database_path: str):
    conn = sqlite3.connect(database_path)
    conn.cursor().execute("drop table if exists main")
