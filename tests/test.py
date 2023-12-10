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
    def test_save_BaesModel(self):
        """test save_Basemodel"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_doc(self):
        """ Tests doc """
        self.assertisNotNone(BaseModel.__doc__)

    def test_to_json(self):
        '''test to jason'''

if __name__ == '__main__':
    unittest.main()
