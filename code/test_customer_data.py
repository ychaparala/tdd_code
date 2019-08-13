#!/usr/bin/env python
#
###########################################
#
# File: test_customer_data.py
# Author: Ra Inta
# Description:
# Created: July 28, 2019
# Last Modified: July 28, 2019
#
###########################################


import unittest

from customer_data import Customer


class TestCustomerData(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.customer1 = Customer("beeble", "bsmith@itsme.com", 350, 7)
        self.customer2 = Customer("KarenRulz", "kaz@yolo.com", 5, 2)

    def test_account_positive(self):
        print("test_account_positive")
        self.assertTrue(self.customer1.account_balance >= 0)
        self.assertTrue(self.customer2.account_balance >= 0)

    def test_purchase_level(self):
        print("test_purchase_level")
        self.customer1.purchase_level(2)
        self.customer2.purchase_level(1)

        self.assertEqual(self.customer1.level, 9)
        self.assertEqual(self.customer1.account_balance, 350 - 2*10)
        self.assertEqual(self.customer2.level, 3)
        self.assertEqual(self.customer2.account_balance, 5 - 1*10)


if __name__ == '__main__':
    unittest.main()





###########################################
# End of test_customer_data.py
###########################################
