#!/usr/bin/python3
"""class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects"""
        object_n = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_n, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        all_obj = FileStorage.__objects
        objec = {obj: all_obj[obj].to_dict() for obj in all_obj.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objec, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objec = json.load(f)
                for obj in objec.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
