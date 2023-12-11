#!/usr/bin/python3
"""unittests for city"""
from models.city import City
import os
import models
from time import sleep
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """Unittests for City class."""

    def test_type(self):
        """Unittests for testing City class"""
        self.assertEqual(City, type(City()))

    def test_id_type(self):
        """Unittests for testing City class"""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_a_datetime(self):
        """Unittests for testing City class"""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_a_datetime(self):
        """Unittests for testing City class"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_storage_value(self):
        """Unittests for testing City class"""
        self.assertIn(City(), models.storage.all().values())

    def test_state_id_is_public_class_attribute(self):
        """Unittests for testing City class"""
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        """Unittests for testing City class"""
        ct = City()
        self.assertEqual(str, type(City.name))
        self.assertNotIn("name", ct.__dict__)

    def test_uuid(self):
        """Unittests for testing City class"""
        City1 = City()
        City2 = City()
        self.assertNotEqual(City1.id, City2.id)

    def test_cities_different_created_at(self):
        """Unittests for testing City class"""
        City1 = City()
        sleep(0.08)
        City2 = City()
        self.assertLess(City1.created_at, City2.created_at)

    def test_cities_different_updated_at(self):
        """Unittests for testing City class"""
        City1 = City()
        sleep(0.08)
        City2 = City()
        self.assertLess(City1.updated_at, City2.updated_at)

    def test_args_with_none(self):
        """Unittests for testing City class"""
        City1 = City(None)
        self.assertNotIn(None, City1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Unittests for testing City class"""
        date_iso = datetime.today().isoformat()
        City1 = City(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(City1.id, "vf5v1")
        self.assertEqual(City1.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(City1.updated_at, datetime.fromisoformat(date_iso))

    def test_raises_with_None_kwargs(self):
        """Unittests for testing City class"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for save method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "file")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("file", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        """Unittests for testing City class"""
        City1 = City()
        with self.assertRaises(TypeError):
            City1.save(None)

    def test_delayed_save(self):
        """Unittests for testing City class"""
        City1 = City()
        sleep(0.08)
        _updated_at = City1.updated_at
        City1.save()
        self.assertLess(_updated_at, City1.updated_at)

    def test_save_updates_file(self):
        """Unittests for testing City class"""
        City1 = City()
        City1.save()
        City_id = "City." + City1.id
        with open("file.json", "r") as f:
            self.assertIn(City_id, f.read())

    def test_two_delayed_saves(self):
        """Unittests for testing City class"""
        City1 = City()
        sleep(0.08)
        first_updated_at = City1.updated_at
        City1.save()
        second_updated_at = City1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        City1.save()
        self.assertLess(second_updated_at, City1.updated_at)


class TestCity_to_dict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_type_to_dict(self):
        """Unittests for testing City class"""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_with_none_arg(self):
        """Unittests for testing City class"""
        City1 = City()
        with self.assertRaises(TypeError):
            City1.to_dict(None)

    def test_correct_keys(self):
        """Unittests for testing City class"""
        City1 = City()
        self.assertIn("__class__", City1.to_dict())
        self.assertIn("updated_at", City1.to_dict())
        self.assertIn("id", City1.to_dict())
        self.assertIn("created_at", City1.to_dict())

    def test_to_dict_datetime_str(self):
        """Unittests for testing City class"""
        City1 = City()
        self.assertEqual(str, type(City1.to_dict()["id"]))
        self.assertEqual(str, type(City1.to_dict()["created_at"]))
        self.assertEqual(str, type(City1.to_dict()["updated_at"]))

    def test_to_dict_add(self):
        """Unittests for testing City class"""
        City1 = City()
        City1.name = "marouane"
        City1.number = 1
        self.assertIn("number", City1.to_dict())
        self.assertEqual("marouane", City1.name)

    def test_contrast_to_dict_dunder_dict(self):
        """Unittests for testing City class"""
        City1 = City()
        self.assertNotEqual(City1.to_dict(), City1.__dict__)


if __name__ == "__main__":
    unittest.main()
