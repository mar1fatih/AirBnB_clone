#!/usr/bin/python3
""" Tests Amenity """

import unittest
import os
import pep8
import datetime
from models import amenity
Amenity = amenity.Amenity

class Test_Amenity(unittest.TestCase):
    """ Tests amenity """

    def test_pep8(self):
        """ Tests the pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Check pep
        """
    class Test_Place(unittest.TestCase):
    """ Tests Place """

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Check pep8")


    def test_Place_dict(self):
        """ Place_dict """
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('__class__' in self.place.__dict__)

    def test_save_Place(self):
        """ Save_Place """
        self.place.save()

if __name__ == '__main__':
    unittest.main()
