#!/usr/bin/python3
""" python file that contains the class definition of a State """

from sqlalchemy import Integer, String, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base

Mymetadata = MetaData()
Base = declarative_base(metadata=Mymetadata)


class State(Base):
    """ class of State """
    __tablename__ = 'state'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
