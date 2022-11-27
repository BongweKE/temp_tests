#!/usr/bin/env python3
"""
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
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

    def test_city_id(self):
        ''' Tests for city_id attribute.'''

        # TPLAC-CI: test if city_id is a string object
        self.assertIs(type(Place.city_id), str)

    def test_user_id(self):
        ''' Tests for user_id attribute.'''

        # TPLAC-UI: test if city_id is a string object
        self.assertIs(type(Place.user_id), str)

    def test_name(self):
        ''' Tests for name attribute.'''

        # TPLAC-NM: test if name is a string object
        self.assertIs(type(Place.name), str)

    def test_description(self):
        ''' Tests for description attribute.'''

        # TPLAC-DS: test if description is a string object
        self.assertIs(type(Place.description), str)

    def test_number_rooms(self):
        ''' Tests for number_rooms attribute.'''

        # TPLAC-NR: test if name is an int object
        self.assertIs(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        ''' Tests for number_bathrooms attribute.'''

        # TPLAC-NB: test if number_bathrooms is an int object
        self.assertIs(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        ''' Tests for max_guest attribute.'''

        # TPLAC-MG: test if max_guest is an int object
        self.assertIs(type(Place.max_guest), int)

    def test_price_by_night(self):
        ''' Tests for price_by_night attribute.'''

        # TPLAC-PN: test if price_by_night is an int object
        self.assertIs(type(Place.price_by_night), int)

    def test_latitude(self):
        ''' Tests for latitude attribute.'''

        # TPLAC-LA: test if latitude is a float object
        self.assertIs(type(Place.latitude), float)

    def test_longitude(self):
        ''' Tests for longitude attribute.'''

        # TPLAC-LO: test if longitude is a float object
        self.assertIs(type(Place.longitude), float)

    def test_amenity_ids(self):
        ''' Tests for amenity_ids attribute.'''

        # TPLAC-AI: test if amenity_ids is a list object
        self.assertIs(type(Place.amenity_ids), list)
    # +++++++++++++++++++++++
    # end test for attributes
    # +++++++++++++++++++++++
