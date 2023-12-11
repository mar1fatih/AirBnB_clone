#!/usr/bin/python3
"""unittests for user.py"""
from models.user import User
from datetime import datetime
import unittest
import models
import os
from time import sleep


class TestUser(unittest.TestCase):
    """ testing User class """

    def test_type(self):
        """function to test User class"""
        self.assertEqual(User, type(User()))

    def test_id_type(self):
        """function to test User class"""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_a_datetime(self):
        """function to test User class"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_a_datetime(self):
        """function to test User class"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_storage_value(self):
        """function to test User class"""
        self.assertIn(User(), models.storage.all().values())

    def test_first_name(self):
        """function to test User class"""
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """function to test User class"""
        self.assertEqual(str, type(User.last_name))

    def test_email(self):
        """function to test User class"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """function to test User class"""
        self.assertEqual(str, type(User.password))

    def test_users_different_created_at(self):
        """function to test User class"""
        User1 = User()
        sleep(0.08)
        User2 = User()
        self.assertLess(User1.created_at, User2.created_at)

    def test_users_different_updated_at(self):
        """function to test User class"""
        User1 = User()
        sleep(0.08)
        User2 = User()
        self.assertLess(User1.updated_at, User2.updated_at)

    def test_args_with_none(self):
        """function to test User class"""
        User1 = User(None)
        self.assertNotIn(None, User1.__dict__.values())

    def test_uuid(self):
        """function to test User class"""
        User1 = User()
        User2 = User()
        self.assertNotEqual(User1.id, User2.id)

    def test_None_kwargs(self):
        """function to test User class"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        """function to test User class"""
        date_iso = datetime.today().isoformat()
        User1 = User(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(User1.id, "vf5v1")
        self.assertEqual(User1.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(User1.updated_at, datetime.fromisoformat(date_iso))


class TestUser_todict(unittest.TestCase):
    """testing to_dict method"""

    def test_type_to_dict(self):
        """function to test User class"""
        self.assertTrue(dict, type(User().to_dict()))

    def test_with_arg(self):
        """function to test User class"""
        User1 = User()
        with self.assertRaises(TypeError):
            User1.to_dict(None)

    def test_correct_keys(self):
        """function to test User class"""
        User1 = User()
        self.assertIn("__class__", User1.to_dict())
        self.assertIn("id", User1.to_dict())
        self.assertIn("created_at", User1.to_dict())
        self.assertIn("updated_at", User1.to_dict())

    def test_to_dict_datetime_str(self):
        """function to test User class"""
        User1 = User()
        self.assertEqual(str, type(User1.to_dict()["id"]))
        self.assertEqual(str, type(User1.to_dict()["created_at"]))
        self.assertEqual(str, type(User1.to_dict()["updated_at"]))

    def test_to_dict_added_attributes(self):
        """function to test User class"""
        User1 = User()
        User1.name = "marouane"
        User1.number = 1
        self.assertEqual("marouane", User1.name)
        self.assertIn("number", User1.to_dict())

    def test_dif_dict(self):
        """function to test User class"""
        User1 = User()
        self.assertNotEqual(User1.to_dict(), User1.__dict__)


class TestUser_save(unittest.TestCase):
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
        """function to test User class"""
        User1 = User()
        with self.assertRaises(TypeError):
            User1.save(None)

    def test_delayed_save(self):
        """function to test User class"""
        User1 = User()
        sleep(0.08)
        _updated_at = User1.updated_at
        User1.save()
        self.assertLess(_updated_at, User1.updated_at)

    def test_updates_file(self):
        """function to test User class"""
        User1 = User()
        User1.save()
        User_id = "User." + User1.id
        with open("file.json", "r") as f:
            self.assertIn(User_id, f.read())


if __name__ == "__main__":
    unittest.main()
