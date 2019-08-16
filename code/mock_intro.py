#!/usr/bin/env python
#
###########################################
#
# File: mock_intro.py
# Author: Ra Inta
# Description:
# Created: August 15, 2019
# Last Modified: August 15, 2019
#
###########################################

# Import the library
from unittest.mock import Mock

# Instansiate the object. So flexible!
mock_obj = Mock()

mock_obj

# Create a Customer class from the customer_data module:
Customer = Mock()

# Check attributes
Customer.account_balance

# Check methods
Customer.purchase_level(2)

# Assert the method was actually called
Customer.purchase_level.assert_called()

# Check if it wasn't---should get a warning!
Customer.purchase_level.assert_not_called()


###########################################
# End of mock_intro.py
###########################################
