#!/usr/bin/env python3
""" Test module for FileStorage class.
"""
from models import storage


class TestFileStorage(unittest.TestCase):
    """ TestCase implementation for FileStorage class
    """
    # -----------------------
    # start tests for methods
    # -----------------------

    def setUp(self):
        ''' Sets up the environment for each test method.'''

    def test_objects(self):
        ''' Tests the __objects attribute.'''

        # TFILE-OB: test that type of __object is dict
        self.assertIs(type(storage.all()), dict)
    # ------------------------
    # end of tests for methods
    # ------------------------

    # ++++++++++++++++++++++++++
    # start tests for attributes
    # ++++++++++++++++++++++++++
# =========ATTRIBUTE TESTS HERE=======
    # +++++++++++++++++++++++
    # end test for attributes
    # +++++++++++++++++++++++
