#!/usr/bin/env python
#
###########################################
#
# File: test_logging.py
# Author: Ra Inta
# Description:
# Created: June 06, 2019
# Last Modified: June 06, 2019
#
###########################################

import logging

output_to_file = False

if not output_to_file:
    logging.basicConfig(level=logging.DEBUG,
                        format=' %(asctime)s ----- %(levelname)s ----- %(message)s')
else:
    logging.basicConfig(filename='test_logging.log',
                        level=logging.DEBUG,
                        format=' %(asctime)s ----- %(levelname)s ----- %(message)s')

logging.debug('Start of program')


def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug(f'i is {i} total is {total}')
        logging.debug(f'End of factorial({n})')
        return total


print(factorial(5))

logging.debug('End of program')

###################################################
#Level | Logging Function | Description
#
#DEBUG | logging.debug() | The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
#INFO | logging.info() | Used to record information on general events in your program or confirm that things are working at their point in the program.
#WARNING | logging.warning() | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
#ERROR | logging.error() | Used to record an error that caused the program to fail to do something.
#CRITICAL | logging.critical() | The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
###################################################



logging.debug('Some debugging details.')
logging.info('Function seems to be working just fine')
logging.warning('An error is about to be logged')
logging.error('An error had occurred')
logging.critical('The system has GONE CRITICAL!')



###########################################
# End of test_logging.py
###########################################
