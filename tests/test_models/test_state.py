#!/usr/bin/python3
"""unittests for state.py"""
from models.state import State
from datetime import datetime
import unittest
import models
import os
from time import sleep


class TestState(unittest.TestCase):
    """testing State class"""

    def test_type(self):
        """unittest for testing State class"""
        self.assertEqual(State, type(State()))

    def test_id_type(self):
        """unittest for testing State class"""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_a_datetime(self):
        """unittest for testing State class"""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_a_datetime(self):
        """unittest for testing State class"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_storage_value(self):
        """unittest for testing State class"""
        self.assertIn(State(), models.storage.all().values())

    def test_name_is_public_class_attribute(self):
        """unittest for testing State class"""
        State1 = State()
        self.assertEqual(str, type(State.name))
        self.assertNotIn("name", State1.__dict__)
        self.assertIn("name", dir(State1))

    def test_uuid(self):
        """unittest for testing State class"""
        State1 = State()
        State2 = State()
        self.assertNotEqual(State1.id, State2.id)

    def test_states_different_created_at(self):
        """unittest for testing State class"""
        State1 = State()
        sleep(0.08)
        State2 = State()
        self.assertLess(State1.created_at, State2.created_at)

    def test_args_with_none(self):
        """unittest for testing State class"""
        State1 = State(None)
        self.assertNotIn(None, State1.__dict__.values())

    def test_states_different_updated_at(self):
        """unittest for testing State class"""
        State1 = State()
        sleep(0.08)
        State2 = State()
        self.assertLess(State1.updated_at, State2.updated_at)

    def test_None_kwargs(self):
        """unittest for testing State class"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        """unittest for testing State class"""
        date_iso = datetime.today().isoformat()
        State1 = State(id="vf5v1", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(State1.id, "vf5v1")
        self.assertEqual(State1.created_at, datetime.fromisoformat(date_iso))
        self.assertEqual(State1.updated_at, datetime.fromisoformat(date_iso))


class TestState_save(unittest.TestCase):
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
        """unittest for testing State class"""
        State1 = State()
        with self.assertRaises(TypeError):
            State1.save(None)

    def test_delayed_save(self):
        """unittest for testing State class"""
        State1 = State()
        sleep(0.08)
        _updated_at = State1.updated_at
        State1.save()
        self.assertLess(_updated_at, State1.updated_at)

    def test_updates_file(self):
        """unittest for testing State class"""
        State1 = State()
        State1.save()
        State_id = "State." + State1.id
        with open("file.json", "r") as f:
            self.assertIn(State_id, f.read())

    def test_two_saves(self):
        """unittest for testing State class"""
        State1 = State()
        sleep(0.08)
        first_updated_at = State1.updated_at
        State1.save()
        second_updated_at = State1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.08)
        State1.save()
        self.assertLess(second_updated_at, State1.updated_at)


class TestState_todict(unittest.TestCase):
    """testing to_dict method"""

    def test_type_to_dict(self):
        """unittest for testing State class"""
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_with_arg(self):
        """unittest for testing State class"""
        State1 = State()
        with self.assertRaises(TypeError):
            State1.to_dict(None)

    def test_correct_keys(self):
        """unittest for testing State class"""
        State1 = State()
        self.assertIn("__class__", State1.to_dict())
        self.assertIn("id", State1.to_dict())
        self.assertIn("created_at", State1.to_dict())
        self.assertIn("updated_at", State1.to_dict())

    def test_to_dict_datetime_str(self):
        """unittest for testing State class"""
        State1 = State()
        self.assertEqual(str, type(State1.to_dict()["id"]))
        self.assertEqual(str, type(State1.to_dict()["created_at"]))
        self.assertEqual(str, type(State1.to_dict()["updated_at"]))

    def test_to_dict_added_attributes(self):
        """unittest for testing State class"""
        State1 = State()
        State1.name = "marouane"
        State1.number = 1
        self.assertEqual("marouane", State1.name)
        self.assertIn("number", State1.to_dict())

    def test_dif_dict(self):
        """unittest for testing State class"""
        State1 = State()
        self.assertNotEqual(State1.to_dict(), State1.__dict__)


if __name__ == "__main__":
    unittest.main()
