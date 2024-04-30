#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    eg_ = create_engine(f'mysql+mysqldb://{username}:\
                        {password}@localhost:3306/{db_name}')
    Base.metadata.bind = eg_
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    ctz = ssn_.query(City).order_by(City.id).all()

    for x in ctz:
        print(f"{x.id}: {x.name} -> {x.state.name}")

    ssn_.close()
