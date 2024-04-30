#!/usr/bin/python3
"""module doc"""

import sys
import MySQLdb
"""doc"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cr_ = db.cursor()

    try:
        cr_.execute("SELECT * FROM states ORDER BY id ASC")
        output = cr_.fetchall()
        for x in output:
            print(x)

    except Exception as y:
        print(y)

    db.close()
