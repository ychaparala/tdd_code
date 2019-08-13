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

# import unittest
# NOTE: there is no need to import unittest or other special library
# to write the code for pytest


def test_positive():
    print("test_positive")
    assert 3*2 > 0
    assert not -3*2 > 0

def test_is_float():
    print("test_is_float")
    assert type(float(5)) is float
    assert not type(int(5)) is float

def test_addition():
    print("test_addition")
    a = 3
    b = 4
    assert a + b ==  7
    assert not a + b == 0


###########################################
# End of test_numerical.py
###########################################
