#!/usr/bin/python3
<<<<<<< HEAD
"""create a unique FileStorage instance for your application"""
=======
"""This module instantiates an object of class FileStorage"""
>>>>>>> a5f24d014f40095306e3d5a903f7bf5879961ffc
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
