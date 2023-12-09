#!/usr/bin/python3
"""unittests for amenity"""
import os
from models.amenity import Amenity
import models
import unittest
from datetime import datetime
from time import sleep


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity class."""

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_type(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_a_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_a_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_storage_value(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_name_is_public_class_attribute(self):
        new = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertNotIn("name", new.__dict__)

    def test_uuid(self):
        ame1 = Amenity()
        ame2 = Amenity()
        self.assertNotEqual(ame1.id, ame2.id)

    def test_two_amenities_different_created_time(self):
        amenity1 = Amenity()
        sleep(0.08)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_amenities_different_updated_time(self):
        amenity1 = Amenity()
        sleep(0.08)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_args_with_none(self):
        amenity1 = Amenity(None)
        self.assertNotIn(None, amenity1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        date_iso = datetime.today().isoformat()
        am = Amenity(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(am.id, "vf5v1")
        self.assertEqual(am.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(am.updated_at, datetime.fromisoformat(date_iso))

    def test_raises_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class Test_to_dict_Amenity(unittest.TestCase):
    """Unittests to_dict method for amenity"""

    def test_type_to_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_with_none_arg(self):
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            amenity1.to_dict(None)

    def test_correct_keys(self):
        amenity1 = Amenity()
        self.assertIn("__class__", amenity1.to_dict())
        self.assertIn("updated_at", amenity1.to_dict())
        self.assertIn("id", amenity1.to_dict())
        self.assertIn("created_at", amenity1.to_dict())

    def test_to_dict_datetime_str(self):
        amenity1 = Amenity()
        amenity1 = amenity1.to_dict()
        self.assertEqual(str, type(amenity1["id"]))
        self.assertEqual(str, type(amenity1["created_at"]))
        self.assertEqual(str, type(amenity1["updated_at"]))

    def test_to_dict_add(self):
        amenity1 = Amenity()
        amenity1.f_name = "marouane"
        amenity1.number = 1
        self.assertIn("number", amenity1.to_dict())
        self.assertEqual("marouane", amenity1.f_name)

    def test_to_dict_diff_dict(self):
        amenity1 = Amenity()
        self.assertNotEqual(amenity1.to_dict(), amenity1.__dict__)


class Test_save_amenity(unittest.TestCase):
    """testing save method"""

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

    def test_none_arg_save(self):
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            amenity1.save(None)

    def test_delayed_save(self):
        amenity1 = Amenity()
        sleep(0.05)
        _update = amenity1.updated_at
        amenity1.save()
        self.assertLess(_update, amenity1.updated_at)

    def test_save_updates_file(self):
        amenity1 = Amenity()
        amenity1.save()
        amenity_id = "Amenity." + amenity1.id
        with open("file.json", "r") as fl:
            self.assertIn(amenity_id, fl.read())

    def test_two_delayed_saves(self):
        amenity1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity1.updated_at
        amenity1.save()
        second_updated_at = amenity1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity1.save()
        self.assertLess(second_updated_at, amenity1.updated_at)


if __name__ == "__main__":
    unittest.main()
