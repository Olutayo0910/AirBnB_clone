#!/usr/bin/python3
"""This module that defines all common attributes/methods for other classes"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This class defines all common attributes/methods for other classe"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args: Unused
            **kwargs (dict): Key/value pairs of attributes.
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.
                                     __name__, self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        :return:dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
