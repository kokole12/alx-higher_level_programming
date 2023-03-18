#!/usr/bin/python3
"""
    Python script that prints out all the states
    containting letter a using sqlalchemy
"""

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    """
        Connecting to the database and runnig the query on
        the database
    """

    database_conect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(database_conect)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    for state in states:
        print('{}: {}'.format(state.id, state.name))
