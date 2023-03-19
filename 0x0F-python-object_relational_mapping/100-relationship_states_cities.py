#!/usr/bin/python3
"""
    Python script to create a state and a city
    using sqlalchmey
"""

from relationship_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City


if __name__ == "__main__":
    """
        Connecting to the database
        creating object of city
        creating object of state
        committing to database
    """

    database_connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connection)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = State(name='California')
    city = City(name = 'San Francisco')
    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
