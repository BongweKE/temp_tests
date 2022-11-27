#!/usr/bin/env python3
"""
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    """
    # -----------------------
    # start tests for methods
    # -----------------------
# =========METHOD TESTS HERE==========
    # ------------------------
    # end of tests for methods
    # ------------------------

    # ++++++++++++++++++++++++++
    # start tests for attributes
    # ++++++++++++++++++++++++++

    def test_name(self):
        ''' Tests for name attribute.'''

        A = Amenity()
        # TAMEN-NM: test if name is a string object
        self.assertIs(type(A.name), str)
    # +++++++++++++++++++++++
    # end test for attributes
    # +++++++++++++++++++++++
