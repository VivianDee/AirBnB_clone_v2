#!/usr/bin/python3
"""This module instantiates an object of either of the following classes:

DBStorage: Which is a storage class which stores objects in a MySQL database
           which uses the SQAlchemy orm to create, read, update or delete
           objects in the database

FileStorage: Which is a storage class which stores objects in a json file
"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review

from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
