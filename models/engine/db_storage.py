#!/usr/bin/python3
"""import modules"""

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """new class"""
    __engine =  None
    __session = None

    def __init__(self):
        """init function"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all function"""
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        objects = {}
        for x in classes:
            for obj in self.__session.query(x).all():
                