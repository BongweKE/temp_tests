#!/usr/bin/env python3
""" 
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
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

        C = City()

        # TAMEN-NM: test if name is a string object
        self.assertIs(type(C.name), str)

    def test_state_id(self):
        ''' Tests for state_id attribute.'''
        C = City()

        # TAMEN-SI: test if state_id is a string
        self.assertIs(type(C.state_id), str)
    # +++++++++++++++++++++++
    # end test for attributes
    # +++++++++++++++++++++++
