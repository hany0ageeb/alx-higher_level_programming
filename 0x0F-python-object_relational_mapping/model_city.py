#!/usr/bin/python3
"""
model_city
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", ForeignKey('states.id'), nullable=False)
    state = relationship("State")
