import sqlite3
from datetime import datetime

def writeCalculations(n1, n2, operation):

    con = sqlite3.connect("database.db")
    try:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f".{datetime.now().microsecond // 1000:03d}"

        currentTotal = getCurrentTotal()
        if getCurrentTotal() == None:
            exit
        else:
            match operation:
                case "add":
                    total = currentTotal + (n1 + n2)
                case "sub":
                    total = currentTotal + (n1 - n2)
                case "mul":
                    total = currentTotal + (n1 * n2)
                case "div":
                    if n2 != 0:
                        total = currentTotal + (n1 / n2)
                    else:
                        print("Error: Division by zero.")
                        return
                case _:
                    print(f"Invalid operation: {operation}")
                    return
  
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

def getCurrentTotal():
    con = sqlite3.connect("database.db")
    try:
        cursor = con.execute("SELECT total FROM calculations order by date desc limit 1;")
        for row in cursor:
            return row[0]

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        con.close()