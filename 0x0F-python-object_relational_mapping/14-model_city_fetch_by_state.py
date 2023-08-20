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
    Query = session.query(City.id.label('id'), City.name.label
                          ('name'), State.name.label('state')).join(
                           State).filter(City.state_id ==
                                         State.id).order_by(City.id)
    for i in Query:
        print(f"{i.state}: ({i.id}) {i.name}")
