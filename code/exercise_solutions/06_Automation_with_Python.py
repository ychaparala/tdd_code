#!/home/ra/anaconda3/bin/python
#
###########################################
#
# File: automation_and_glob.py
# Author: Ra Inta, for BH Analytics, LLC, and Accelebrate, Inc.
# Description:
# Created: October 12, 2018
# Last Modified: October 12, 2018
#
###########################################

import glob
import pandas as pd
import sqlite3

# Some of the data are in Excel worksheets:
xls_files = glob.glob('../../data/*/*.xlsx')

print("Excel files: {0}".format(xls_files))

# Import the first worksheet as a DataFrame:
df_staff = pd.read_excel(xls_files[0])

# And some data are in an SQL database (here, an SQLite db):
db_file_list = glob.glob('../../data/*/*.sql')

print("SQL files: {0}".format(db_file_list))

# Open a database connection and obtain two dataframes from two tables within:
cnx = sqlite3.connect(db_file_list[0])

# The data are stored as two tables in the db:
df_patient = pd.read_sql_query("SELECT * FROM patient", cnx)
df_visits = pd.read_sql_query("SELECT * FROM outpatient", cnx)

# close the db connection
cnx.close()

# Perform some transformations on the resulting dataframes:
print("Sample of Staff data: \n\n{0}\n\n".format(df_staff.sample(5)))

print("Sample of Visit data: \n\n{0}\n\n".format(df_visits.sample(5)))

# Let's join visits and staff to see who was working on each visit:
df_merged = pd.merge(df_visits, df_staff, how='left', on='StaffID')

print("Sample of merged data: \n\n{0}\n\n".format(df_merged.sample(5)))

# The staff did a great job. Let's send this to HR!
# Output the result as an Excel file
out_col_names = ["VisitID", "StaffID", "VisitDate", "FirstName",
"LastName", "HourlyRate", "Salary", "PayType", "StaffType", "StaffReportsTo"]

print("Be patient! This can take some time, because there are over 44,000 rows...")

df_merged.to_excel("staff_for_hr.xlsx", sheet_name='staff_info', columns=out_col_names, header=True, index=False)

# or a CSV file:
df_merged.to_csv("staff_for_hr.csv", columns=out_col_names, header=True, index=False)

print("\n\nOK, done!\nYou can send the Excel files to HR whenever you're ready.")

###########################################
# End of automation_and_glob.py
###########################################
