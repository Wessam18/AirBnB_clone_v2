#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey, Integer, Float 
from sqlalchemy.orm import relationship
import os



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        city_id = column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = column(String(60), ForeignKey("users.id"), nullable=False)
        name = column(String(128), nullable=False)
        description = column(String(1024), nullable=True)
        number_rooms = column(Integer, nullable=False, defualt=0)
        number_bathrooms = column(Integer, nullable=False, defualt=0)
        max_guest = column(Integer, nullable=False, defualt=0)
        price_by_night = column(Integer, nullable=False, defualt=0)
        latitude = column(Float, nullable=True)
        longitude = column(Float, nullable=True)
        reviews = relationship('Review', cascade='all, delete-orphan', backref='place')


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

    @property
    def reviews(self):
        """reviews attribute"""
        from models import storage
        from models.review import Review
        reviews_list = []
        for i in storage.all(Review).values():
            if i.place.id == self.id:
                reviews_list.append(i)
        return reviews_list
