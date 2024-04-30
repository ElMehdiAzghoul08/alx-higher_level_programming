#!/usr/bin/python3
"""module doc"""

import sys
import MySQLdb
"""doc"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306, user=username,
                             passwd=password, db=db_name)
        cr_ = db.cursor()
        cr_.execute("SELECT ctz_.id, ctz_.name, states.name \
                    FROM ctz_ JOIN states ON ctz_.state_id = states.id \
                    ORDER BY ctz_.id ASC")
        output = cr_.fetchall()
        for x in output:
            print(x)

        db.close()

    except Exception as y:
        print(f"MySQL Error [{y.args[0]}]: {y.args[1]}")
