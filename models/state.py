#!/usr/bin/python3
""" This module defines all attributes and methods of the State class """
import models
from models.base_model import BaseModel


class State(BaseModel):
    """ Implementation for State class """
    skeys = ["name"]

    def __init__(self, *args, **kwargs):
        """ Initializing new State class """
        super().__init__(**{key: kwargs.get(key) for key in kwargs.keys()
                            if key not in State.skeys
                            and kwargs.get(key) is not None})
        self.name = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in State.skeys:
                    self.__dict__[key] = value
