import sqlite3

DB_PATH = r"A:/path/to/db/file"

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]

    return {key: value for key, value in zip(fields, row)}

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        connection.row_factory = dict_factory

    except sqlite3.Error as e:
        print(e)

    return connection