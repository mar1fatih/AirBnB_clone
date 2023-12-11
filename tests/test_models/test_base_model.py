#!/usr/bin/python3
"""unittests for BaseModel"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class"""

    def test_type(self):
        """ unittest testing base_model """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_type(self):
        """ unittest testing base_model """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_a_datetime(self):
        """ unittest testing base_model """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_a_datetime(self):
        """ unittest testing base_model """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_storage_value(self):
        """ unittest testing base_model """
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_uuid(self):
        """ unittest testing base_model """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_two_base_different_created_time(self):
        """ unittest testing base_model """
        base1 = BaseModel()
        sleep(0.08)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_two_base_different_updated_time(self):
        """ unittest testing base_model """
        base1 = BaseModel()
        sleep(0.08)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_args_with_none(self):
        """ unittest testing base_model """
        base1 = BaseModel(None)
        self.assertNotIn(None, base1.__dict__.values())

    def test_with_None_kwargs(self):
        """ unittest testing base_model """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_kwargs(self):
        """ unittest testing base_model """
        date_iso = datetime.today().isoformat()
        am = BaseModel(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(am.id, "vf5v1")
        self.assertEqual(am.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(am.updated_at, datetime.fromisoformat(date_iso))


class TestBaseModel_save(unittest.TestCase):
    """testing save method"""

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

    def test_none_arg_sav(self):
        """ unittest testing base_model """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_delayed_save(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        sleep(0.08)
        _updated_at = Base1.updated_at
        Base1.save()
        self.assertLess(_updated_at, Base1.updated_at)

    def test_save_file(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        Base1.save()
        Base_id = "BaseModel." + Base1.id
        with open("file.json", "r") as fl:
            self.assertIn(Base_id, fl.read())

    def test_two_saves(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        sleep(0.05)
        first_updated_at = Base1.updated_at
        Base1.save()
        second_updated_at = Base1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        Base1.save()
        self.assertLess(second_updated_at, Base1.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests to_dict method for BaseModel"""

    def test_type_to_dict(self):
        """ unittest testing base_model """
        self.assertTrue(dict, type(BaseModel().to_dict()))

    def test_to_dict_with_none_arg(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        with self.assertRaises(TypeError):
            Base1.to_dict(None)

    def test_correct_keys(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        self.assertIn("__class__", Base1.to_dict())
        self.assertIn("created_at", Base1.to_dict())
        self.assertIn("id", Base1.to_dict())
        self.assertIn("updated_at", Base1.to_dict())

    def test_to_dict_datetime_str(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        Base1 = Base1.to_dict()
        self.assertEqual(str, type(Base1["id"]))
        self.assertEqual(str, type(Base1["created_at"]))
        self.assertEqual(str, type(Base1["updated_at"]))

    def test_to_dict_contains_added_attributes(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        Base1.name = "marouane"
        Base1.number = 1
        self.assertIn("number", Base1.to_dict())
        self.assertEqual("marouane", Base1.name)

    def test_contrast_to_dict_dunder_dict(self):
        """ unittest testing base_model """
        Base1 = BaseModel()
        self.assertNotEqual(Base1.to_dict(), Base1.__dict__)


if __name__ == "__main__":
    unittest.main()
