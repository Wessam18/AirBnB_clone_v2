#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    place_amenity = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False)
    )

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                'Review', cascade='all, delete-orphan', backref='place')
        amenities = relationship(
                'Amenity', secondary='place_amenity', viewonly=False)

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

    @property
    def amenities(self):
        """Getter attribute returns list of Amenity instances"""
        from models import storage
        amenities_list = []
        for amenity_id in self.amenity_ids:
            am = storage.get('Amenity', amenity_id)
            if am:
                amenities_list.append(am)
        return amenities_list

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute that handles appending Amenity IDs."""
        from models.amenity import Amenity
        if isinstance(amenity, Amenity):
            if amenity.id not in self.amenity_ids:
                self.amenity_ids.append(amenity.id)
        else:
            pass  # Do nothing if the object is not an Amenity
