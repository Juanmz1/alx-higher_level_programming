#!/usr/bin/python3
""" script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for new_states in session.query(State.name, City.id,
            City.name).filter(State.id == City.id):
        print(new_states[0] + ":(" +str(new_states[1]) + ") " + new_states[2])
