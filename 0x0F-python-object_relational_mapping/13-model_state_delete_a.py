#!/usr/bin/python3
"""
    Python script to delete all states
    cotaining letter a using sqlalchemy
"""

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
        Connecting to the database and
        deleting the states
    """

    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter(State.name.contains('a'))

    if states is not None:
        for state in states:
            session.delete(state)

    session.connit()

    session.close()
