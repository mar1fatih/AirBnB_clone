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
        self.add()

    def test_save_Place(self):
        """ Save_Place """
        self.place.save()

if __name__ == '__main__':
    unittest.main()
