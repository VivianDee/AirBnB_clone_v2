#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "file":
        name = ""
    else:
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete-orphan', back_ref="state")

    @property
    def cities(self):
    """Returns the list of City instances with state_id"""
    import models
    objs = models.storage.all("City")
    city = []

    for obj in objs.values():
        try:
            if obj.state_id == self.id:
                city.append(obj)
        except Exception:
            pass
    return city
