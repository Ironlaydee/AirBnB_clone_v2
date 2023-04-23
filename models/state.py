#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("city", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        value_city = models.storage.all()
        lst = []
        city_list = []
        for key in value_city:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'city'):
                lst.append(value_city[key])
        for obj in lst:
            if (obj.state_id == self.id):
                city_list.append(obj)
        return (city_list)
