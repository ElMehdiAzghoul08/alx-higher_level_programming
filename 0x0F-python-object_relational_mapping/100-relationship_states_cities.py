#!/usr/bin/python3
"""creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
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
    Base.metadata.create_all(eg_)
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    ssn_.add(california)
    ssn_.add(san_francisco)

    ssn_.commit()
    ssn_.close()
