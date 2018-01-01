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


def clear_db(database_path: str):
    conn = sqlite3.connect(database_path)
    conn.cursor().execute("drop table if exists main")


def run_sql_query(database: str, sqlquery: str):
    print("SQL query: ", sqlquery)
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(sqlquery)
    sqloutput = cur.fetchall()
    print(sqloutput)
    return
