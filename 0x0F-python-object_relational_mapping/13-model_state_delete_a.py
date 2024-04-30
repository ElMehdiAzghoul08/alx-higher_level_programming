#!/usr/bin/python3
"""script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    eg_ = create_engine(f'mysql+mysqldb://{username}:\
                        {password}@localhost:3306/{db_name}')
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    statess_a = ssn_.query(State).filter(State.name.like('%a%')).all()
    for x in statess_a:
        ssn_.delete(x)

    ssn_.x()
    ssn_.close()
