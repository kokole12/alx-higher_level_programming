#!/usr/bin/python3
"""
    modeling a class for city
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State, Base


class City(Base):
    """
        Initializing the class for city
        Arguments:
            __tablename__: name of the table
            state_id: foreign key to state
            name: name of the city
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
