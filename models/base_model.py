#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """constractor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.fromisoformat(v)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """print the class instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.__dict__["created_at"].isoformat()
        dict_copy["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dict_copy
