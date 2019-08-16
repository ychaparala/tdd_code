###########################################
#
# File: 05_Exercises_Pandas_Data_Management.py
# Created: July 15, 2018
# Last Modified: July 8, 2019
# Author: Ra Inta and Evan Carey, written for BH Analytics, LLC
###########################################


## 1) Start by writing the import statements for pandas and numpy. Also, set up the
## working directory to point at the folder you have established for this class. Confirm
## the working directory is what you expect.
import pandas as pd
import os

os.getcwd()  # See your current working directory
os.chdir("path/to/your/directory")
# os.chdir(r"C:\Users\evancarey\Dropbox\Work")
os.getcwd()  # Check you're in the right place


## 2) Import the three datasets mentioned above (lookup, user, and campaign):
## a. First inspect the text file with a text editor


## b. Import the dataset and save the result

# You may have to change the following to point correctly at your files:
campaign_df = pd.read_csv("Data/Data_Sims/phishing/Campaign.csv")
lookup_df = pd.read_csv("Data/Data_Sims/phishing/Lookup.csv")
user_df = pd.read_csv("Data/Data_Sims/phishing/User.csv")

## c. Check the resulting files: how many rows and columns?
campaign_df.shape  # 40 rows, 3 columns
lookup_df.shape  # 24,000 rows, 10 columns
user_df.shape  # 2,000 rows, 10 columns


## 3) Write some basic subset and manipulations for these files:
## a. Print the first 5 rows of each file using .head()

campaign_df.head()
lookup_df.head()
user_df.head()

## b. In the user table, subset the table to only the males and print the result. How
## many rows of ‘Males’ are there? Repeat this for females.
user_df[user_df["Gender"] == 'male'].shape[0]  # 1002 rows
user_df[user_df["Gender"] == 'female'].shape[0]  # 998 rows


## c. Use .loc() to subset to the first 5 rows and the first two columns of the user
## table
user_df.loc[0:4,'UserID':'EmailAddress']  # Note the slicing index includes the end-point

# If you look at help(user_df.loc):
# "note that contrary to usual python slices, **both** the start and the stop
# are included!"

## d. Use .iloc() to subset to the first 5 rows and the first two columns of the user
## table
user_df.iloc[0:5,0:2]
# Note the slicing indices are different for .iloc[] : they don't include the end

###########################################
# End of 05_Exercises_Pandas_Data_Management.py
###########################################
