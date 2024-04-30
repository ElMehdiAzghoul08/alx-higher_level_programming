#!/usr/bin/python3
"""script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

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

    statess_ = ssn_.query(State).order_by(State.id).all()

    for x in statess_:
        print(f"{x.id}: {x.name}")
        for y in x.ctz:
            print(f"    {y.id}: {y.name}")

    ssn_.close()
