#!/usr/bin/python3
<<<<<<< HEAD
"""This is the amenity class"""
=======
""" State Module for HBNB project """
>>>>>>> a5f24d014f40095306e3d5a903f7bf5879961ffc
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
