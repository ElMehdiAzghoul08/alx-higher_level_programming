#!/usr/bin/python3
"""module doc"""

import sys
import MySQLdb
"""doc"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_state = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306, user=username, passwd=password,
                             db=db_name)

        cr_ = db.cursor()

        qr_ = "SELECT ctz_.name FROM ctz_ JOIN states \
            ON ctz_.state_id = states.id WHERE states.name = %s ORDER BY \
                ctz_.id ASC"
        cr_.execute(qr_, (name_state,))
        output = cr_.fetchall()
        if output:
            ct_ = ', '.join(cty_[0] for cty_ in output)
            print(ct_)
        else:
            print("no ctz found")

        db.close()

    except Exception as y:
        print(f"MySQL Error [{y.args[0]}]: {y.args[1]}")
