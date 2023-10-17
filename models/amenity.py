#!/usr/bin/python3
""" This module defines all attributes and methods of the Amenity class """
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Implementation for Amenity class """
    akeys = ["name"]

    def __init__(self, *args, **kwargs):
        """ Initializing new Amenity class """
        super().__init__(**{key: kwargs.get(key) for key in kwargs.keys()
                            if key not in Amenity.akeys
                            and kwargs.get(key) is not None})
        self.name = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in Amenity.akeys:
                    self.__dict__[key] = value
