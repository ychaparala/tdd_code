#!/usr/bin/env python
#
###########################################
#
# File: mock_makingTests.py
# Author: Ra Inta
# Description:
# Created: August 15, 2019
# Last Modified: August 15, 2019
#
###########################################

from customer_data import Customer
from unittest.mock import Mock

# Generate some Customer examples:
customer1 = Customer("beeble", "bsmith@itsme.com", 350, 7)
customer2 = Customer("KarenRulz", "kaz@yolo.com", 5, 2)
Customer = Mock()



def test_account_positive():
    assertTrue(customer1.account_balance >= 0)
    assertTrue(customer2.account_balance >= 0)


###########################################
# End of mock_makingTests.py
###########################################
