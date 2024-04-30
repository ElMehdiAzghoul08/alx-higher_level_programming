#!/usr/bin/python3
"""script that lists all State objects
that contain the letter a
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    eg_ = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                        format(username, password, db_name),
                        pool_pre_ping=True)
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    statess_a = ssn_.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for x in statess_a:
        print("{}: {}".format(x.id, x.name))

    ssn_.close()
