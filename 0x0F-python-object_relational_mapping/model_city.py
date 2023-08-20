#!/usr/bin/python3
""" python file that contains the class definition of a City """

from sqlalchemy import Integer, String, Column, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = dclarative_base()

class City(Base):
    """ class of city """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
