#!/usr/bin/python3
"""
    Python script to fetch all cities
"""

from sys import argv
from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    """
        Connecting to the database and fetching all the cities
    """
    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()
    results = session.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
