i#!/usr/bin/python3
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
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
