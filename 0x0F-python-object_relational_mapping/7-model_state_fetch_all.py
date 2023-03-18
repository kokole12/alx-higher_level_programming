#!/usr/bin/python3
"""
    Script that runs and returns all states
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':

    """
        access to the database to fetch state
    """

    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3], pool_pre_ping=True)

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
