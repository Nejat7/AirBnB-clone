#!/usr/bin/python3
<<<<<<< HEAD
"""Module file_storage
This Module contains a definition for FileStorage Class
"""


import importlib
import json
import os
import re


class FileStorage:
    """FileStorage Class
    Attributes:
        __file_path (str): string - path to the JSON file
=======
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
>>>>>>> 6e82d82d7a43d2fd7dc8a7171301ff513ec8f578
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if (os.path.isfile(self.__file_path)
                and os.path.getsize(self.__file_path) > 0):
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: self.get_class(k.split(".")[0])(**v)
                                  for k, v in json.load(f).items()}

    def get_class(self, name):
        """ returns a class from models module using its name"""
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)
=======
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
>>>>>>> 6e82d82d7a43d2fd7dc8a7171301ff513ec8f578
