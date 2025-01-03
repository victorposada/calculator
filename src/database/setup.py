import sqlite3
from datetime import datetime

def createDatabase():
    con = sqlite3.connect("database.db")
    try:
        con.execute("""
            create table if not exists calculations (
                id integer primary key autoincrement,
                n1 real,
                n2 real,
                operation string,
                date date,
                total real
            )
        """)
        print("Table database created")

    except sqlite3.Error as e:
        print(f"Error create table: {e}")
    finally:
        con.close()


def setupInitialValues():
    con = sqlite3.connect("database.db")
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        n1 = 0
        n2 = 0
        total = 0
        operation = "setup"
        con.execute("INSERT INTO calculations (n1, n2, operation, date, total) VALUES (?, ?, ?, ?, ?)", (n1, n2, operation, date, total))
        con.commit()
        print("Values inserted successfully")

        cursor = con.execute("SELECT * FROM calculations")
        print("Table content:")
        for row in cursor:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        con.close()
