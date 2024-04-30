#!/usr/bin/python3
"""doc define class City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """doc"""
    __tablename__ = 'ctz_'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    id_of_state = Column(Integer, ForeignKey('states.id'), nullable=False)
