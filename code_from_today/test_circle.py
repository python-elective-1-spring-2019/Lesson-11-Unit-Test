import unittest
from math import pi
from circle import area


class TestCircle(unittest.TestCase):
    
    def test_area(self):
        # test when radius is >= 0
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0.0)
        self.assertAlmostEqual(area(2.1), pi * 2.1**2)

    def test_values(self):
        # test if a ValueError is raised when nessesary
        self.assertRaises(ValueError, area, -2)

    def test_type(self):
        # Test if r is of type int or float
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'Error')
        self.assertRaises(TypeError, area, [])