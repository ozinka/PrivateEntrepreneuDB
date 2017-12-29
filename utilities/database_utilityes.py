import sqlite3

def create_db():
    # TODO: create database
    pass


def save_to_db(dct: dict):
    f = open("result.txt", 'a')
    f.write(str(dct) + '\n')
    f.close()


def find_by_name():
    # TODO: find record in db by name
    pass
