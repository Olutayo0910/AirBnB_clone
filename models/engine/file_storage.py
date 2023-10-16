#!/usr/bin/python3
"""The filestorage module"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """The filestorage is an abstracted storage engine
    Attr:
    __file_path (str): stores the objects
    __objects (dict): saves the dictionary of the instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        key = "{}.{}".format(ocname, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file(__file_path)"""
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for value in obj_dict.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
