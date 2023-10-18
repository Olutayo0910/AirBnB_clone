#!/usr/bin/python3
""" This module defines all attributes and methods of the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Implementation for Amenity class
    Attributes:
        name(str): amenity name

    """
    name = ""
