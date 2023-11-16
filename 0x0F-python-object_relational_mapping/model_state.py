#!/usr/bin/python3
"""
file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in the database.

    Attributes:
        id (int): An auto-generated, unique integer and primary key.
        name (str): A string with a maximum length of 128 characters.

    Args:
        Base (class): The SQLAlchemy declarative base class.

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
