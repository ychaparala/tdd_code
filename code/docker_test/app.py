#!/usr/bin/env python
#
###########################################
#
# File: app.py
# Author: Ra Inta
# Description:  Had to rewrite the app!
# Created: August 13, 2019
# Last Modified: August 13, 2019
#
###########################################

import numpy as np

print("It's dark!\nYou're likely to be eaten by a grue...\n\n")

def roll20():
    """Just another twenty sided die rolling example.
    This time, we give some nice output for extreme
    rolls."""
    roll = np.random.randint(1, 21)
    if roll == 20:
        print("Critical hit!!")
    elif roll == 1:
        print("Critical miss. Oh no!")
    return roll


def attack_the_grue(n):
    print("You attack the grue!")
    if n > 15:
        print("You won!")
    elif n < 5:
        print("Oh no! You missed...")
    if n == 1:
        print("You were EATEN BY THE GRUE!!!")


attack_the_grue(roll20())

###########################################
# End of app.py
###########################################
