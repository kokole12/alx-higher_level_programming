#!/usr/bin/python3
"""
    This a script that defines the class State and
    base mapping of delcarative Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """
        The state calss
        Attribute:
            __tablename__ (str): name of the table
            id: the id assigned to each state
            name: the name of the state
    """

    __tablename__ = 'state'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
