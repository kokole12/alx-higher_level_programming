#!/usr/bin/python3
"""
    scritpt to add a new state
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    """
        connecting to the database
    """

    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print('{0}'.format(state.id))
    session.close()
