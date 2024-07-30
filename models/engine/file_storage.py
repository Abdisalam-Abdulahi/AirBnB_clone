#!/usr/bin/python3
"""
    deserialization and serialization handler
"""
from models.base_model import BaseModel
import json
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
# import os.path


class FileStorage:
    """
     deserialization and serialization class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = (obj)

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        raw = FileStorage.__objects
        objDi = {obj: raw[obj].to_dict() for obj in raw.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objDi, file)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        try:
            # if os.path.isfile(path):
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
