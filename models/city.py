#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
   """ The city class, contains state ID and name """
   __tablename__ = 'cities'
   
   if getenv('HBTN_TYPE_STORAGE') == 'db':
      name = Column(String(128), nullable=False)
      state_id = Column(String(60), ForeignKey('States.id'), nullable=False)
      places = relationship('Place', cascade='all, delete', backref='cities')
   else:
      name = ""
      state_id = ""

