#!/usr/bin/python3
"""This module instantiates an object of either of the following classes:

DBStorage: Which is a storage class which stores objects in a MySQL database
           which uses the SQAlchemy orm to create, read, update or delete
           objects in the database

FileStorage: Which is a storage class which stores objects in a json file
"""

from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity

from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
