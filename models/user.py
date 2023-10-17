#!/usr/bin/python3
""" This module defines all attributes and methods of the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Implementation for User class
    Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    ukeys = ["email", "password", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        """ Initializing new User class """
        super().__init__(**{key: kwargs.get(key) for key in kwargs.keys()
                            if key not in User.ukeys
                            and kwargs.get(key) is not None})
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in User.ukeys:
                    self.__dict__[key] = value
