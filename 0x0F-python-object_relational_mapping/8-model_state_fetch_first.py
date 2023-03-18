#!/usr/bin/python3
"""
    The script runs a query using sqlachemy to return the fist
    record
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    """
        Connecting to the database
    """

    database_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_connect)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id).first():
        if State is not None:
            print('{}: {}'.format(instance.id, instance.name))
        else:
            print("Nothing")

