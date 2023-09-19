#!/usr/bin/python3
"""Defines DBStorage class which stores objects to a MySQL Database"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self._models = {
            "State": State, "City": City, "User": User,
            "Place": Place, "Review": Review, "Amenity": Amenity}

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session)

        All objects depending of the class name (argument cls) if cls=None,
        Query all types of objects (User, State, City, Amenity, Place & Review)

        Args:
            cls (any, optional): class name. Defaults to None.

        Returns:
            dict: objects in database
        """
        obj_dict = {}
        if cls:
            # get the class from the self._models dict
            _class = self._models.get(cls)
            query = self.__session.query(_class)

            for model_obj in query:
                key = "{}.{}".format(type(model_obj).__name__, model_obj.id)
                obj_dict[key] = model_obj

        else:
            # using the values of the dict self.models to get all class objs.
            # The values are class definitions
            for _class in self._models.values():
                for model_obj in self.__session.query(_class):
                    key = "{}.{}".format(
                        type(model_obj).__name__, model_obj.id)
                    obj_dict[key] = model_obj

        return obj_dict

    def new(self, obj):
        """Adds a new object to the DB"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the DB"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configures the session for communication with the DB"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factory=session)
        self.__session = session()

    def close(self):
        """Closes the session"""
        self.__session.close()
