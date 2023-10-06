#!/usr/bin/python3
<<<<<<< HEAD
'''
    Define the class Place.
'''
=======
<<<<<<< HEAD
""" Place Module for HBNB project """
import os
=======
"""Defines the Place class."""
import models
>>>>>>> 035e0065cc2af0641ad4ddf322075c593e5ae710
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from models.base_model import BaseModel, Base
# from models.amenity import Amenity
=======
>>>>>>> ccb9566893d1dff77b0278c64c6bcf074c69909a
>>>>>>> 035e0065cc2af0641ad4ddf322075c593e5ae710

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

<<<<<<< HEAD
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

<<<<<<< HEAD
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))
=======
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals
            to the current Place.id."""

            reviews = list(models.storage.all(Review).values())

            return list(
                filter(lambda review: (review.place_id == self.id), reviews))

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on
            the attribute amenity_ids that contains all Amenity.id."""

            amenities = list(models.storage.all(Amenity).values())

            return list(
                filter(lambda amenity: (amenity.place_id in self.amenity_ids),
                       amenities))

        @amenities.setter
        def amenities(self, value=None):
            """Adds ids in amenity_ids ."""
            if type(value) == type(Amenity):
=======
association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))
>>>>>>> 035e0065cc2af0641ad4ddf322075c593e5ae710


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
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
            '''
                Return list: review instances if Review.place_id==curr place.id
                FileStorage relationship between Place and Review
            '''
            list_reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            '''
                Return list: amenity inst's if Amenity.place_id=curr place.id
                FileStorage many to many relationship between Place and Amenity
            '''
            list_amenities = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return list_amenities

        @amenities.setter
<<<<<<< HEAD
        def amenities(self, amenity=None):
            '''
                Set list: amenity instances if Amenity.place_id==curr place.id
                Set by adding instance objs to amenity_ids attribute in Place
            '''
            if amenity:
                for amenity in models.storage.all(Amenity).values():
                    if amenity.place_id == self.id:
                        amenity_ids.append(amenity)
=======
        def amenities(self, value):
            if type(value) == Amenity:
>>>>>>> ccb9566893d1dff77b0278c64c6bcf074c69909a
                self.amenity_ids.append(value.id)
>>>>>>> 035e0065cc2af0641ad4ddf322075c593e5ae710
