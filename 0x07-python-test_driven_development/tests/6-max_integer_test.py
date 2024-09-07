#!/usr/bin/python3
"""
UnitTest Module For Max_Integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxTestCase(unittest.TestCase):
    """
    Unit test cases for max_integer function
    """

    def test_max_integer(self):
        # Test with regular lists
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

        # Test with negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list containing a single element
        self.assertEqual(max_integer([5]), 5)

        # Test with an empty list
        self.assertEqual(max_integer([]), None)

    def test_max_integer_with_mixed_types(self):
        # Test with a list containing a string should raise TypeError
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'str', 4])

    def test_max_integer_with_none(self):
        # Test if None is passed in the list
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2, 3])

    def test_max_integer_with_same_elements(self):
        # Test with a list where all elements are the same
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_integer_with_floats(self):
        # Test with a list containing floats
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_max_integer_with_mixed_ints_floats(self):
        # Test with a list containing both integers and floats
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_max_integer_with_one_element(self):
        # Test with a list containing one element
        self.assertEqual(max_integer([10]), 10)


if __name__ == '__main__':
    unittest.main()
