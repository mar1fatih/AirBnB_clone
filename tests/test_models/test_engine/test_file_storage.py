#!/usr/bin/python3
"""unittests for file_storage"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest
from datetime import datetime
import os
import models


class TestFileStorage(unittest.TestCase):
    """testing FileStorage class"""

    def test_file_path_Type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_Error_Raise(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def testFileStorage_objects_Type(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """testing methods"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "file")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("file", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_new(self):
        Base = BaseModel()
        User1 = User()
        City1 = City()
        Amenity1 = Amenity()
        State1 = State()
        Place1 = Place()
        Review1 = Review()
        models.storage.new(Base)
        models.storage.new(City1)
        models.storage.new(Place1)
        models.storage.new(State1)
        models.storage.new(Review1)
        models.storage.new(User1)
        models.storage.new(Amenity1)
        all_keys = models.storage.all().keys()
        all_values = models.storage.all().values()
        self.assertIn("User." + User1.id, all_keys)
        self.assertIn(User1, all_values)
        self.assertIn("Place." + Place1.id, all_keys)
        self.assertIn(Place1, all_values)
        self.assertIn("State." + State1.id, all_keys)
        self.assertIn(State1, all_values)
        self.assertIn("Review." + Review1.id, all_keys)
        self.assertIn(Review1, all_values)
        self.assertIn("City." + City1.id, all_keys)
        self.assertIn(City1, all_values)
        self.assertIn("Amenity." + Amenity1.id, all_keys)
        self.assertIn(Amenity1, all_values)
        self.assertIn("BaseModel." + Base.id, all_keys)
        self.assertIn(Base, all_values)

    def test_save(self):
        text = ""
        Base = BaseModel()
        User1 = User()
        City1 = City()
        Amenity1 = Amenity()
        State1 = State()
        Place1 = Place()
        Review1 = Review()
        models.storage.new(Base)
        models.storage.new(City1)
        models.storage.new(Place1)
        models.storage.new(State1)
        models.storage.new(Review1)
        models.storage.new(User1)
        models.storage.new(Amenity1)
        models.storage.save()
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("City." + City1.id, text)
            self.assertIn("Amenity." + Amenity1.id, text)
            self.assertIn("User." + User1.id, text)
            self.assertIn("State." + State1.id, text)
            self.assertIn("BaseModel." + Base.id, text)
            self.assertIn("Review." + Review1.id, text)
            self.assertIn("Place." + Place1.id, text)

    def test_reload(self):
        Base = BaseModel()
        User1 = User()
        City1 = City()
        Amenity1 = Amenity()
        State1 = State()
        Place1 = Place()
        Review1 = Review()
        models.storage.new(Base)
        models.storage.new(City1)
        models.storage.new(Place1)
        models.storage.new(State1)
        models.storage.new(Review1)
        models.storage.new(User1)
        models.storage.new(Amenity1)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Review." + Review1.id, objs)
        self.assertIn("BaseModel." + Base.id, objs)
        self.assertIn("State." + State1.id, objs)
        self.assertIn("User." + User1.id, objs)
        self.assertIn("Place." + Place1.id, objs)
        self.assertIn("City." + City1.id, objs)
        self.assertIn("Amenity." + Amenity1.id, objs)
        

    def test_reload_Raises(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_all_Error(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_Raises(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), "hi")

    def test_save_Raises(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)


if __name__ == "__main__":
    unittest.main()
