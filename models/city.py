#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    
    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        state_id = column(String(60), nullable=False, ForeignKey=True)
        name = column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete-orphan', backref='cities')

    else:
        state_id = ""
        name = ""
