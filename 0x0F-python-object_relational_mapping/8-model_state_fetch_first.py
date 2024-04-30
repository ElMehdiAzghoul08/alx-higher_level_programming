#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

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

    state_one = ssn_.query(State).order_by(State.id).first()
    if state_one:
        print("{}: {}".format(state_one.id, state_one.name))
    else:
        print("Nothing")

    ssn_.close()
