#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """Tests for city. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

class Test_PEP8(unittest.TestCase):
    """Tests for pep8 style."""

    def test_pep8_user(self):
        """Checks pycodestyle"""
        pepstyle = pycodestyle.StyleGuide(quiet=True)
        result = pepstyle.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle incompliant")

class TestCity(unittest.TestCase):
    """Test the city class"""

    @classmethod
    def setClass(cls):
        """Set up class for test"""
        cls.city = City()
        cls.city.name = "NA"
        cls.city.state_id = "ST"

    @classmethod
    def tearDown(self):
        """Deletes the test after completion."""
        del cls.city

    def test_attributes_City(self):
        """ Checks for attributes in City. """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attribute_type(self):
        """ Tests for attribute type for City. """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

if __name__ == "__main__":
    unittest.main()
