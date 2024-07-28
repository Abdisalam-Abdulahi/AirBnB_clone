#!/usr/bin/python3
"""
    deserialization and serialization handler
"""
# from models import base_model
import json
import os.path


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
        path = "/home/cabdisalam/ALX_projects/AirBnB_clone"
        if os.path.isfile(path):
            with open(FileStorage.__file_path, "r") as file:
                objDi = json.load(file)
                for val in objDi.values():
                    className = val[__class__]
                    del val[__class__]
                    self.new(eval(className)(**val))
