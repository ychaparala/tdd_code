#!/usr/bin/env python
#
###########################################
#
# File: test_numerical.py
# Author: Ra Inta
# Description:
# Created: July 28, 2019
# Last Modified: July 28, 2019
#
###########################################

import unittest


class TestNumerical(unittest.TestCase):
    """Tests a few numerical properties, including positivity,
    whether a number is a float and some addition properties.

    This is meant to be run as a program from the command-line.
    Either run with:
        python test_numerical.py -v
    Or, if you are running from a *nix operating system, the above shebang may
    work, so you can instead run:
        ./test_numerical.py -v
    """

    def test_positive(self):
        print("test_positive")
        self.assertTrue(3*2 > 0)
        self.assertFalse(-3*2 > 0)

    def test_is_float(self):
        print("test_is_float")
        self.assertTrue(type(float(5)) is float)
        self.assertFalse(type(int(5)) is float)

    def test_addition(self):
        print("test_addition")
        a = 3
        b = 4
        self.assertEqual(a + b, 7)
        self.assertNotEqual(a + b, 0)

if __name__ == '__main__':
    unittest.main()



###########################################
# End of test_numerical.py
###########################################
