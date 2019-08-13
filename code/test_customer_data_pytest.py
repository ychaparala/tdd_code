#!/usr/bin/env python
#
###########################################
#
# File: test_customer_data_pytest.py
# Author: Ra Inta
# Description:
# Created: July 28, 2019
# Last Modified: July 28, 2019
#
###########################################


from customer_data import Customer

customer1 = Customer("beeble", "bsmith@itsme.com", 350, 7)
customer2 = Customer("KarenRulz", "kaz@yolo.com", 5, 2)

def test_account_positive():
    print("test_account_positive")
    assert customer1.account_balance >= 0
    assert customer2.account_balance >= 0

def test_purchase_level():
    print("test_purchase_level")
    customer1.purchase_level(2)
    customer2.purchase_level(1)

    assert customer1.level == 9
    assert customer1.account_balance == 350 - 2*10
    assert customer2.level == 3
    assert customer2.account_balance == 5 - 1*10





###########################################
# End of test_customer_data_pytest.py
###########################################
