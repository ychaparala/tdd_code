#!/usr/bin/env python
#
###########################################
#
# File: unittest_demo.py
# Author: Ra Inta
# Description:
# Created: July 28, 2019
# Last Modified: July 28, 2019
#
###########################################

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        #self.assertEqual('foo'.upper(), 'FOOi')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



if __name__ == '__main__':
    unittest.main()



###########################################
# End of unittest_demo.py
###########################################
