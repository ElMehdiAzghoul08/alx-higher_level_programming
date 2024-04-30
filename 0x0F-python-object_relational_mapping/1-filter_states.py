#!/usr/bin/python3
import sys
import MySQLdb
"""doc"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)
    cr_ = db.cursor()

    try:
        cr_.execute("SELECT * FROM states WHERE name \
                    LIKE 'N%' ORDER BY id ASC")
        output = cr_.fetchall()
        for x in output:
            print(x)

    except Exception as y:
        print(y)

    db.close()
