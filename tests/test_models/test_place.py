#!/usr/bin/python3
"""unittests for place.py"""
import os
import unittest
import models
from models.place import Place
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """Unittests for Place class."""

    def test_type(self):
        """Unittests for testing Place class"""
        self.assertEqual(Place, type(Place()))

    def test_id_type(self):
        """Unittests for testing Place class"""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_a_datetime(self):
        """Unittests for testing Place class"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_a_datetime(self):
        """Unittests for testing Place class"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_storage_value(self):
        """Unittests for testing Place class"""
        self.assertIn(Place(), models.storage.all().values())

    def test_with_None_kwargs(self):
        """Unittests for testing Place class"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_args_with_none(self):
        """Unittests for testing Place class"""
        Place1 = Place(None)
        self.assertNotIn(None, Place1.__dict__.values())

    def test_city_id(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(Place1))
        self.assertNotIn("city_id", Place1.__dict__)

    def test_description_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(Place1))
        self.assertNotIn("desctiption", Place1.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(Place1))
        self.assertNotIn("number_rooms", Place1.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(Place1))
        self.assertNotIn("number_bathrooms", Place1.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(Place1))
        self.assertNotIn("user_id", Place1.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(Place1))
        self.assertNotIn("price_by_night", Place1.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(Place1))
        self.assertNotIn("amenity_ids", Place1.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(Place1))
        self.assertNotIn("longitude", Place1.__dict__)

    def test_name_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Place1))
        self.assertNotIn("name", Place1.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(Place1))
        self.assertNotIn("max_guest", Place1.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(Place1))
        self.assertNotIn("latitude", Place1.__dict__)

    def test_uuid(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        Place2 = Place()
        self.assertNotEqual(Place1.id, Place2.id)

    def test_base_different_created_time(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        sleep(0.08)
        Place2 = Place()
        self.assertLess(Place1.created_at, Place2.created_at)

    def test_base_different_updated_time(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        sleep(0.08)
        Place2 = Place()
        self.assertLess(Place1.updated_at, Place2.updated_at)

    def test_instantiation_with_kwargs(self):
        """Unittests for testing Place class"""
        date_iso = datetime.today().isoformat()
        Place1 = Place(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Place1.id, "vf5v1")
        self.assertEqual(Place1.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(Place1.updated_at, datetime.fromisoformat(date_iso))


class TestPlaceSave(unittest.TestCase):
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

    def test_none_arg_sav(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        with self.assertRaises(TypeError):
            Place1.save(None)

    def test_delayed_save(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        sleep(0.08)
        _updated_at = Place1.updated_at
        Place1.save()
        self.assertLess(_updated_at, Place1.updated_at)

    def test_save_file(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        Place1.save()
        Place_id = "Place." + Place1.id
        with open("file.json", "r") as f:
            self.assertIn(Place_id, f.read())

    def test_two_saves(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        sleep(0.08)
        first_updated_at = Place1.updated_at
        Place1.save()
        second_updated_at = Place1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.08)
        Place1.save()
        self.assertLess(second_updated_at, Place1.updated_at)


class TestPlaceToDict(unittest.TestCase):
    """testing to_dict method"""

    def test_type_to_dict(self):
        """Unittests for testing Place class"""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_with_none_arg(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        with self.assertRaises(TypeError):
            Place1.to_dict(None)

    def test_correct_keys(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertIn("__class__", Place1.to_dict())
        self.assertIn("id", Place1.to_dict())
        self.assertIn("created_at", Place1.to_dict())
        self.assertIn("updated_at", Place1.to_dict())

    def test_to_dict_datetime_str(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertEqual(str, type(Place1.to_dict()["id"]))
        self.assertEqual(str, type(Place1.to_dict()["created_at"]))
        self.assertEqual(str, type(Place1.to_dict()["updated_at"]))

    def test_to_dict_contains_added_attributes(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        Place1.name = "marouane"
        Place1.number = 1
        self.assertIn("number", Place1.to_dict())
        self.assertEqual("marouane", Place1.name)

    def test_dif_dict(self):
        """Unittests for testing Place class"""
        Place1 = Place()
        self.assertNotEqual(Place1.to_dict(), Place1.__dict__)


if __name__ == "__main__":
    unittest.main()
