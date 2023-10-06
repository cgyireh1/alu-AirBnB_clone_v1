#!/usr/bin/python3
<<<<<<< HEAD
'''
    Implementing of the Amenity class
'''
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
=======
<<<<<<< HEAD
""" State Module for HBNB project """
import os
=======
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
>>>>>>> 035e0065cc2af0641ad4ddf322075c593e5ae710
from sqlalchemy.orm import relationship
>>>>>>> ccb9566893d1dff77b0278c64c6bcf074c69909a

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

<<<<<<< HEAD

class Amenity(BaseModel, Base):
<<<<<<< HEAD
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
=======
    """Amenities of a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary="place_amenity")
=======
class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
>>>>>>> ccb9566893d1dff77b0278c64c6bcf074c69909a
>>>>>>> 035e0065cc2af0641ad4ddf322075c593e5ae710
