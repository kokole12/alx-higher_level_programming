#!/usr/bin/python3
"""
    modeling a class for city
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City:
    """
        Initializing the class for city
        Arguments:
            __tablename__: name of the table
            state_id: foreign key to state
            name: name of the city
    """

    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
