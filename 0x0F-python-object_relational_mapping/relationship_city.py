#!/usr/bin/python3
"""
doc that defines class City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """doc class City"""

    __tablename__ = 'ctz'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    id_of_state = Column(Integer, ForeignKey('states.id'), nullable=False)
