#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    #name = column(String(128), nullable=False)
    #cities = relationship("City", cascade="all, delete-orphan", backref="state")

#    @property
 #   def cities(self):
  #      """getter attribute"""
   #     from models import storage
    #    cities_list = []
     #   for i in storage.all(City).values():
      #      if i.state.id == self.id:
       #         cities_list.append(i)
       # return cities_list
