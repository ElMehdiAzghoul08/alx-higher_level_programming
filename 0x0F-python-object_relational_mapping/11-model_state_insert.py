#!/usr/bin/python3
"""script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    eg_ = create_engine(f'mysql+mysqldb://{username}:\
                        {password}@localhost/{db_name}')
    Ssn_ = sessionmaker(bind=eg_)
    ssn_ = Ssn_()

    neo_st = State(name="Louisiana")
    ssn_.add(neo_st)
    ssn_.x()

    print(neo_st.id)

    ssn_.close()
