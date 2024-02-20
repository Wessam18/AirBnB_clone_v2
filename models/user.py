#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy import column, String
from sqlalchemy.orm import relationship
import os

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    
    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        email = column(String(128), nullable=False)
        password = column(String(128), nullable=False)
        first_name = column(String(128), nullable=True)
        last_name = column(String(128), nullable=True)
        places = relationship('Place', cascade='all, delete-orphan', backref='user')
        reviews = relationship('Review', cascade='all, delete-orphan', backref='user')

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
