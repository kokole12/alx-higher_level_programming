#!/usr/bin/python3
"""
    script that returns a state when passed as an argument
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
        Connecting to the databnase
        then fetching from the database
    """

    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()

    if state is not None:
        print('{}'.format(state.id))
    else:
        print("Not found")
