##########################################################################
# File: Python Review Exercises Solution
# Author: Evan Carey, created for BH Analytics
# Purpose: This is the solution to the Python Review Exercises
##########################################################################

# In[0]:
import numpy as np
import pandas as pd


# In[1]:
# 1)
# Make a string from “Hello World”, and assign a variable reference to it.
str1 = "Hello World"

# In[1a]:
# a.
# What is the length of this string? (len function)
len(str1)  # 11

# In[1b]:
# b.
# Take the first 5 letters of this string and assign to a new variable.
first_str = str1[0:5]

# In[1c]:
# c.
# Concatenate that result with the word “big” in the middle, and the last
# part of the string. It should print as: Hello Big World
mid_str = 'Big'
last_str = str1.split(" ")[1]
new_str_list = (first_str, mid_str, last_str)
new_str = (" ".join(new_str_list))
print(new_str)

# or
print(first_str + ' Big ' + str1[-5:])

# In[1d]:
# d.
# Print the new String all Upper case, then in lower case.
print(new_str.upper())
print(new_str.lower())

# In[1e]:
# e.
# Capitalize only the first letter of each word.
print(new_str.title())

# In[2]:
# 2)
# Create two variables named first and last. Assign your first and last name to
# each variable.
first = "John"
last = "Smith"
# In[2a]:
# a.
# Use the string format method to print the following string:
# i. “My first name is _____, my last name is_____”
print("My first name is {}, my last name is {}.".format(first, last))

# In[2b]:
# b.
# Concatenate these two variables together using the “+”, include a space.
full_name = first + " " + last
print(full_name)

# In[2c]:
# c.
# Use string methods to print this new variable all lower case, then all upper
# case, then in capitalized case.
print(full_name.lower())
print(full_name.upper())
print(full_name.capitalize())

# In[2d]:
# d.
# What is the total length of the concatenated variable?
len(full_name)  # 10

# In[2e]:
# e.
# Slice the first letters from each string to create your initials with a period
# following each initial. Print this string.
print(first[0].capitalize() + "." + last[0].capitalize() + ".")

 # or
print(".".join([first[0], last[0], ""]))

# In[2f]:
# f.
# Create a list with these two variables as elements of the list.
names = [first, last]

# In[2g]:
# g.
# Use that list and the following string (“_”) and the .join method to print
# your name like so: First_Last
"_".join(names)

# In[3]:
# 3)
# Establish a file directory for your lab files if you have not already done so.
# Write a string that resolves to this directory.
import os
print("My working directory:\n" + os.getcwd())
os.chdir("/home/ra/host/BH_Analytics/Deloitte_online/code")
print("My new working directory:\n" + os.getcwd())
text_file = open("Output.txt", "w")
text_file.write("This is a string.")
text_file.close()

# In[4]:
# 4)
# Write a Python script: When the user runs the script, prompt the user for
# their name, then print the string “Hello, <name>.”
user1 = input("What is your name? ")
print("Hello,", user1)

# or
print("Hello, " + user1)

# In[5]:
# 5)
# Write a script which asks the user for a lower number and a higher number,
# then calculates and returns the range.
#*For now, assume no user error and do not attempt to handle exceptions.
low_num = input("Enter a lower number: ")
high_num = input("Enter a higher number: ")
print("The range is: " + str(float(high_num) - float(low_num)))

# or
print("The range is:", (float(high_num) - float(low_num)))

# In[6]:
# 6)
# Write a for loop which generates the numbers 1 to 99 (by 3), and squares them
for i in range(1, 99, 3):
    print(i * i)

# In[7]:
# 7)
# Create a list representing the following matrix of data (list of lists)
#*see exercise for matrix
matrix = [[4, 6, 7],
          [3, 5, 7],
          [2, 5, 4]]
# In[7a]:
# a.
# Subset the list down to the 1st row, 1st column.
matrix[0][0]

# In[7b]:
# b.
#	Add the 2nd row, 2nd column to the 3rd row, 3rd column.
matrix[1][1] + matrix[2][2]

# In[7c]:
# c.
# Using a for loop, get the average value for each row of data. Print a message
# in each iteration of the loop stating the average.
    # i.	Hint: use a for loop, the enumerate function, the sum and len
    # functions.

for i, val in enumerate(matrix):
    res = sum(val)/len(val)
    print("The average for row " + str(i) + " is: " + str(res))

# In[7d]:
# d.
# Using a for loop, get the average value for each column of data. Print the
# result in each loop iteration.
    # i.	Hint: this will require a double loop.

for i in range(len(matrix[0])):
    res1 = [x[i] for x in matrix]
    res2 = sum(res1)/len(res1)
    print("The average for column " + str(i + 1) + " is: " + str(res2))


# In[8]:
# 8)
# Use the datetime module in Python to determine what weekday the first of
# each month falls on in 2016. Track your results in a list of tuples, where
# the first element of each tuple is the month and the second element of each
# tuple is the weekday. Finally, print your result using a string format

import datetime

# start with January
datetime.date(2016, 1, 1).weekday()
res_dte = (datetime.date(2016, 1, 1).strftime("%B"),
           datetime.date(2016, 1, 1).strftime("%A"))
print("In 2016, the first day of {0} is a {1}.".format(res_dte[0], res_dte[1]))

# write a loop to extend this to multiple months


def month_weekday(yr, month, day):
    """Takes in year (yr), month and day, as integers,
    and returns the month and day of week, written in full."""
    res_month = datetime.date(yr, month, day).strftime("%B")
    res_day = datetime.date(yr, month, day).strftime("%A")
    res = res_month, res_day
    return(res)

month_weekday(2016, 1, 1)
dt_2016 = [month_weekday(2016, i+1, 1) for i in range(12)]

for i in dt_2016:
    print("In 2016, the first day of {0} is a {1}.".format(i[0], i[1]))

# In[8a]:
# a.
# i.	Add a loop to do this for the years 2012-2016. Track the year in your
# results list in addition to the month and weekday. Print the results
# accordingly
# extend to multiple years.


def yr_month_weekday(yr, month, day):
    """Takes in year (yr), month and day, as integers,
    and returns the year, month and day of week, written in full."""
    res_year = datetime.date(yr, month, day).strftime("%Y")
    res_month = datetime.date(yr, month, day).strftime("%B")
    res_day = datetime.date(yr, month, day).strftime("%A")
    res = res_year, res_month, res_day
    return(res)

dt_all = []

for i in range(2012, 2017):
    dt_all.extend([yr_month_weekday(i, x+1, 1) for x in range(12)])

for i in dt_all:
    print("In {0}, the first day of {1} is a {2}.".format(i[0], i[1], i[2]))

# Extension using dict and keyargs (tuple unpacking)
my_dict = {"yr": ("2012"), "month": ("Jan")}
"test {yr} test {month}".format(**my_dict)

# In[9]:
# 9)
# Using list comprehension and the range function, complete the following tasks:
# In[9a]:
# a.
# Print a list of the numbers -10 through 10.
print([i for i in range(-10, 11)])

# In[9b]:
# b.
# For the numbers in (a) less than -5 or greater than 5, print their squared
# value.
print([i*i for i in range(-10, 11) if i < -5 or i > 5])

# In[9c]:
# c.
# For the numbers in (a) greater than 0, return their square root.

import math

print([math.sqrt(i) for i in range(-10, 11) if i > 0])

# or
print([i**(1/2) for i in range(-10, 11) if i > 0])

# In[9d]:
# d.
# Using the numbers in (a), return the string “NA” if they are less than 0, and
# return the number + 1 if it is 0 or higher.
print(["NA" if i < 0 else i + 1 for i in range(-10, 11)])
