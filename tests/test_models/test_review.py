#!/usr/bin/python3
"""unittests for review"""
import unittest
import models
import os
from models.review import Review
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    """testing Review class"""

    def test_type(self):
        """function to test Review class"""
        self.assertEqual(Review, type(Review()))

    def test_id_type(self):
        """function to test Review class"""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_a_datetime(self):
        """function to test Review class"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_a_datetime(self):
        """function to test Review class"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_storage_value(self):
        """function to test Review class"""
        self.assertIn(Review(), models.storage.all().values())

    def test_text(self):
        """function to test Review class"""
        Review1 = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(Review1))
        self.assertNotIn("text", Review1.__dict__)

    def test_place_id(self):
        """function to test Review class"""
        Review1 = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review1))
        self.assertNotIn("place_id", Review1.__dict__)

    def test_uuid(self):
        """function to test Review class"""
        Review1 = Review()
        Review2 = Review()
        self.assertNotEqual(Review1.id, Review2.id)

    def test_user_id(self):
        """function to test Review class"""
        Review1 = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Review1))
        self.assertNotIn("user_id", Review1.__dict__)

    def test_reviews_different_created_at(self):
        """function to test Review class"""
        Review1 = Review()
        sleep(0.08)
        Review2 = Review()
        self.assertLess(Review1.created_at, Review2.created_at)

    def test_args_with_none(self):
        """function to test Review class"""
        Review1 = Review(None)
        self.assertNotIn(None, Review1.__dict__.values())

    def test_reviews_different_updated_at(self):
        """function to test Review class"""
        Review1 = Review()
        sleep(0.08)
        Review2 = Review()
        self.assertLess(Review1.updated_at, Review2.updated_at)

    def test_instantiation_with_kwargs(self):
        """function to test Review class"""
        date_iso = datetime.today().isoformat()
        Review1 = Review(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Review1.id, "vf5v1")
        self.assertEqual(Review1.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(Review1.updated_at, datetime.fromisoformat(date_iso))

    def test_None_kwargs(self):
        """function to test Review class"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_to_dict(unittest.TestCase):
    """testing to_dict method"""

    def test_type_to_dict(self):
        """function to test Review class"""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_with_none_arg(self):
        """function to test Review class"""
        Review1 = Review()
        with self.assertRaises(TypeError):
            Review1.to_dict(None)

    def test_correct_keys(self):
        """function to test Review class"""
        Review1 = Review()
        self.assertIn("__class__", Review1.to_dict())
        self.assertIn("id", Review1.to_dict())
        self.assertIn("created_at", Review1.to_dict())
        self.assertIn("updated_at", Review1.to_dict())

    def test_to_dict_datetime_str(self):
        """function to test Review class"""
        Review1 = Review()
        self.assertEqual(str, type(Review1.to_dict()["id"]))
        self.assertEqual(str, type(Review1.to_dict()["created_at"]))
        self.assertEqual(str, type(Review1.to_dict()["updated_at"]))

    def test_to_dict_contains_added_attributes(self):
        """function to test Review class"""
        Review1 = Review()
        Review1.name = "marouane"
        Review1.number = 1
        self.assertEqual("marouane", Review1.name)
        self.assertIn("number", Review1.to_dict())

    def test_dif_dict(self):
        """function to test Review class"""
        Review1 = Review()
        self.assertNotEqual(Review1.to_dict(), Review1.__dict__)


class TestReview_save_method(unittest.TestCase):
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
        """function to test Review class"""
        Review1 = Review()
        with self.assertRaises(TypeError):
            Review1.save(None)

    def test_delayed_save(self):
        """function to test Review class"""
        Review1 = Review()
        sleep(0.08)
        _updated_at = Review1.updated_at
        Review1.save()
        self.assertLess(_updated_at, Review1.updated_at)

    def test_save_updates_file(self):
        """function to test Review class"""
        Review1 = Review()
        Review1.save()
        Review_id = "Review." + Review1.id
        with open("file.json", "r") as f:
            self.assertIn(Review_id, f.read())

    def test_two_saves(self):
        """function to test Review class"""
        Review1 = Review()
        sleep(0.08)
        first_updated_at = Review1.updated_at
        Review1.save()
        second_updated_at = Review1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.08)
        Review1.save()
        self.assertLess(second_updated_at, Review1.updated_at)


if __name__ == "__main__":
    unittest.main()
