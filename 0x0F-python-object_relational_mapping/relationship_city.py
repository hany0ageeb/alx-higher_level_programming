#!/usr/bin/python3
"""
model_city
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
