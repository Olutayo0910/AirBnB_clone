#!/usr/bin/python3
""" This module defines all attributes and methods of the City class """
import models
from models.base_model import BaseModel


class City(BaseModel):
    """ Implementation for City class """
    ckeys = ["state_id", "name"]

    def __init__(self, *args, **kwargs):
        """ Initializing new City class """
        super().__init__(**{key: kwargs.get(key) for key in kwargs.keys()
                            if key not in City.ckeys
                            and kwargs.get(key) is not None})
        self.state_id = ""
        self.name = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in City.ckeys:
                    self.__dict__[key] = value
