import time
import argparse
from utilities import general
from utilities import database_utilityes


def main(database: str, db_action: str, xml_file: str):
    if database == "":
        print("-db option is required (for more use -h)")
        return
    print("database is: " + database)
    if db_action == "parse":
        if xml_file == "":
            print("-x option is required (for more use -h)")
            return
        general.parse_xml(xml_file, database)
    if db_action == "create":
        database_utilityes.create_db(database)

    print("action is: " + db_action)
    # print("file to export: " + xml_file)
    start = round(time.clock(), 1)

    end = round(time.clock(), 1)
    print("Total time: ", (end - start), "sec")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Utility for working with Private Entrepreneur DB')
    parser.add_argument("-db", "--database", help="SQLite file name")
    parser.add_argument("-a", "--action", help="Action with database: [parse], [clear], [find]")
    parser.add_argument("-x", "--xmlfile", help="File to import data from")
    # TODO: parser.add_argument("-f", "--action", help="File to import data from")
    args = parser.parse_args()
    database_file = args.database
    database_action = args.action
    xml_file = args.xmlfile
    main(database_file, database_action, xml_file)
