#!/usr/bin/python3
"""
Module: model_state
contains the class definition of a State and an instance
Base = declarative_base()
Attributes:
    Base: module level attribute
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
Base = declarative_base()


class State(Base):
    """
    class State inherits Base
    id (Column): (class attribute)state id
    name (String): (class attribute)state name
    """
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', back_populates='state')
