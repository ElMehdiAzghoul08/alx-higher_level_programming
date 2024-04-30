#!/usr/bin/python3
"""doc define class x"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """doc"""

    __tablename__ = 'ctz'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    id_of_state = Column(Integer, ForeignKey('states.id'), nullable=False)
