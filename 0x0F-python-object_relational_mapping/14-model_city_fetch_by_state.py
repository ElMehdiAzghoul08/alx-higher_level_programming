#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    eg_ = create_engine(f'mysql+mysqldb://{username}:\
                        {password}@localhost:3306/{db_name}')
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    ctz_ = ssn_.query(City).order_by(City.id).all()
    for x in ctz_:
        print("{}: ({}) {}".format(x.state.name, x.id, x.name))

    ssn_.close()
