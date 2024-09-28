import sqlite3

def get_db_connection():
    connection = sqlite3.connect("database.py")
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_db_connection()
    connection.execute('''
    Create table if not exists items(
    id integer primary key autoincrement, 
    name test not null
    description text
    )''')
    connection.commit()
    connection.close()


