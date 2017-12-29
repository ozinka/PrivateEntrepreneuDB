# import os
import argparse


def main(database: str, db_action: str, xmlfile: str):
    print("database is: " + database)
    print("action is: " + db_action)
    print("name to find: " + xmlfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite file name")
    parser.add_argument("-a", "--action", help="Action with database")
    parser.add_argument("-x", "--xmlfile", help="File to import data from")
    # TODO: parser.add_argument("-f", "--action", help="File to import data from")
    args = parser.parse_args()
    database_file = args.database
    database_action = args.action
    xml_file = args.xmlfile
    main(database_file, database_action, xml_file)
