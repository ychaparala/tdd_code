#!/usr/bin/env python
#
###########################################
#
# File: customer_data.py
# Author: Ra Inta
# Description:
# Created: July 28, 2019
# Last Modified: July 28, 2019
#
###########################################


class Customer():
    """Create a Customer for our online game.

    They have an account_balance, which they can use to purchase
    level-ups within the game, via the purchase_level method.
    This increases their level and decreases their account_balance
    according to the current cost of a level."""

    level_cost = 10

    def __init__(self, user_name, email, account_balance, level):
        self.user_name = user_name
        self.email = email
        self.account_balance = account_balance
        self.level = level

    def purchase_level(self, n=1):
        self.account_balance = self.account_balance - n*self.level_cost
        self.level += n



###########################################
# End of customer_data.py
###########################################
