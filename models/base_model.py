#!/usr/bin/python3
"""
Base module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
            Initializer
        Args:
            *args: unused.
            **kwargs: Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
             print: [<class name>] (<self.id>) <self.__dict__>
        """
        className = self.__class__.__name__
        return (f"[{className}] ({self.id}) {self.__dict__}")

    def save(self):
        """
            update the date
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        dictCpy = self.__dict__.copy()
        dictCpy['created_at'] = self.created_at.isoformat()
        dictCpy['updated_at'] = self.updated_at.isoformat()
        dictCpy['__class__'] = self.__class__.__name__
        return dictCpy
