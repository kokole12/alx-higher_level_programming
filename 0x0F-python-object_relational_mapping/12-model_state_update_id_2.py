#!/usr/bin/python3
"""
    Python script that updates the name of a state
    in a database
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    """
        Connecting to the database and
        filtering for the record to be update
    """

    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()

    session.close()
