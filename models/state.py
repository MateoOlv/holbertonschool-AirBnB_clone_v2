#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", 
    cascade="all, delete, delete-orphan", backref="state")

    @property
    def cities(self):
        """"Returns cities that share state.id"""
        from models import storage
        import shlex

        citiesInState = []
        result = []
        for key in storage.all():
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == "City":
                citiesInState.append(storage.all[key])
        for cities in citiesInState:
            if cities.state_id == self.id:
                result.append(cities)
        return result