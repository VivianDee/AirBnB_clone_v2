#!/usr/bin/python3
"""Defines DBStorage class which stores objects to a MySQL Database"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from models.base_model import Base
from models.amenity import Amenity
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
        """Shows all DB objects"""
        new_dict = {}
        for clss in self._models:
            if cls is None or cls is self._models[clss] or cls is clss:
                objs = self.__session.query(self._models[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

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
