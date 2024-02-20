#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey, Integer, Float 
import os



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        city_id = column(String(60), nullable=False, ForeignKey="cities.id")
        user_id = column(String(60), nullable=False, ForeignKey="users.id")
        name = column(String(128), nullable=False)
        description = column(String(1024), nullable=True)
        number_rooms = column(Integer, nullable=False, defualt=0)
        number_bathrooms = column(Integer, nullable=False, defualt=0)
        max_guest = column(Integer, nullable=False, defualt=0)
        price_by_night = column(Integer, nullable=False, defualt=0)
        latitude = column(Float, nullable=True)
        longitude = column(Float, nullable=True)
        amenity_ids = []

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
