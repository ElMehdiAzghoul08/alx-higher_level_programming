#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cr_ = db.cursor()

    try:
        cr_.execute("SELECT * FROM states \
                    WHERE name = %s ORDER BY id ASC", (name_state,))
        output = cr_.fetchall()
        for x in output:
            print(x)

    except Exception as y:
        print(y)

    db.close()
