#!/usr/bin/python3
""" This module defines all attributes and methods of the city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Implementation for city class
    Attributes:
        state_id (str): The state id.
        name(str): city name

    """
    state_id = ""
    name = ""
