#!/usr/bin/python3
"""script that prints the State object
with the name passed as argument
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_statess = sys.argv[4]

    eg_ = create_engine(f'mysql+mysqldb://{username}:\
                        {password}@localhost/{db_name}')
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    statess_ = ssn_.query(State).filter(State.name == name_statess).first()

    if statess_:
        print(statess_.id)
    else:
        print("Not found")

    ssn_.close()
