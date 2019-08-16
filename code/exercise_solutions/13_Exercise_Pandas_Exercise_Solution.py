# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:27:52 2017

@author: Kevin
"""
import pandas as pd
import numpy as np
import os

# where are we?
os.getcwd()

# change to where the files are
os.chdir("/home/ra/host/BH_Analytics/Deloitte_online/data")

# 1. Create a data frame from ex_dm_person_demo.csv,
# and name the data frame “df_person”
# a. Inspect the text file with a text editor
# b. Import the dataset with read_table()
df_person = pd.read_csv('ex_dm_person_demo.csv')

# 2. Do an initial inspection of the dataset
# a. How many rows and columns does it have?
df_person.shape
# 10000 rows x 11 columns

# b. What are the dtypes for each variable in the dataset? (.dtypes attribute)
df_person.dtypes

# 3. Correct the classes of the variables in the dataframe if needed
# a. Age, lab values, and income should be numberic of some type
# all are float64 so OK
# b. Clust_id, Gender, Education, and Outcome should be string
# Note: because pandas stores string as ndarry, they look like object type
# here's how you would convert
df_person['Clust_id'] = df_person['Clust_id'].astype('str')

# c. Make baseline date a date value (to_datetime())
df_person['Baseline_date'] = pd.to_datetime(df_person['Baseline_date'])

# 4. Clean Data
# get some summary statistics
df_person.describe()

# a. Consider the values of “999” and “” to be missing, and code them as such
df_person_columns = list(df_person.columns.values)
for col in df_person_columns:
    if(df_person[col].dtype == np.object):
        if('999' in df_person[col].unique() or '' in df_person[col].unique()):
            print(col)

# only Gender drops out of this
df_person['Gender'].unique()

# you will need to use loc for this - loc works on labels
# iloc works on indexes/positions, ix tries to do loc first, then iloc
# if label not in index
# before
df_person.loc[(df_person['Gender'] == '999'), 'Gender']

# change
df_person.loc[(df_person['Gender'] == '999'), 'Gender'] = np.nan

# after
df_person.loc[(df_person['Gender'] == '999'), 'Gender']

# another option is replace
df_person['Gender'] = df_person['Gender'].replace('999', np.nan)

# b. Check the numeric variables for outliers, code them to be missing
# for grins, set all ages above 100 to na
# before
df_person.loc[(df_person['Age'] > 100), 'Age']
# change
df_person.loc[(df_person['Age'] > 100), 'Age'] = np.nan
# after
df_person.loc[(df_person['Age'] > 100), 'Age']

# c. Lab values should never be below 0. Change any lab values below 0 to be 0.
df_person.loc[(df_person['lab_value_1'] < 0), 'lab_value_1'] = 0
df_person.loc[(df_person['lab_value_2'] < 0), 'lab_value_2'] = 0
df_person.loc[(df_person['lab_value_3'] < 0), 'lab_value_3'] = 0

# 5. Create some new variables…
# a. Lab1_lab2, defined as the ratio of lab1 to lab2
df_person['Lab1_Lab2'] = df_person['lab_value_1'] / df_person['lab_value_2']

# b. edu.cat, with values of “college” (grad and undergrad) and “no college”
df_person['Education'].unique()
# we still have two high schools so combine
df_person.loc[
    (df_person['Education'] == 'High School'),
    'Education'] = 'high school'
# now we can create the new category
df_person['edu.cat'] = np.where(
    df_person['Education'] == 'high school',
    'no college',
    'college')

# c. Create a categorical variable for age based on quartiles (use the cut
# function)
age_bins = (0, 25, 50, 75, 100)
df_person['age_cat'] = pd.cut(df_person.Age, bins=age_bins)

# d. rename the following variables:
# i. gender = sex
df_person = df_person.rename(columns={'Gender': 'Sex'})

# ii. PID = ID
df_person = df_person.rename(columns={'p_id': 'ID'})

# 6. Make a data frame that only includes the following
# variables: P_ID, clust_id, baseline_date
df_person_small = df_person[['ID', 'Clust_id', 'Baseline_date']]

# 7. Make a data frame which only includes the first, fourth,
# and fifth observations (but all variables)
indexes = [0, 3, 4]
df_person_small2 = df_person.ix[indexes]
# OR
df_person_small2 = df_person.ix[[0, 3, 4]]
# OR
df_person_small2 = df_person.iloc[indexes]


########################### end of part 1  ##############################


# 8. Make a data frame which has the first, fourth, and fifth observations,
# and the second and fourth variables
the_obs = [0, 3, 4]
the_vars = [1, 3]

df_person_small3 = df_person.iloc[[0, 3, 4], [1, 3]]

# OR
df_person_small3 = df_person.iloc[the_obs, the_vars]

# 9. Sort your original data frame (dept.data) based on gender, then education,
# then descending income
df_person.sort_index(by=['Sex', 'Education', 'Income'],
                     ascending=[True, True, False])

# Merging Data:
# 10. Create a data frame from the file ex_dm_cluster.csv
# a. Import this with read.csv
df_dept = pd.read_csv('ex_dm_cluster_demo.csv')

# 11. Examine this dataframe
# a. How many unique values of clust_id are present?
# Compare these levels to the unique values of clust_id
# in the person level data frame.
df_dept.shape
df_dept.dtypes
len(df_dept['Clust_id'].unique())
len(df_person['Clust_id'].unique())

# 12. Merge this information back to our original table.
# a. Perform a left join from the cluster table to the person level table.
# You should have all the values from the person level table,
# so the resulting dataframe will be the same size as the original person
# level dataframe. Use the merge function.
df_combined = pd.merge(df_person, df_dept, on='Clust_id', how='left')

# Descriptive Statistics:
# 13. Univariate Statistics:
# a. Describe the date range of baseline date
df_person['Baseline_date'].describe()

# b. What percent of this dataset is Male?
100 * len(df_person.loc[(df_person['Sex'] == 'Male')]) / len(df_person)

# c. What proportion of people have an income above $70,000?
len(df_person.loc[(df_person['Income'] > 70000)]) / len(df_person)

# d. What is the mean age of the dataset?
df_person['Age'].mean()

# 14. Grouping Statistics:
# a. What is the mean income by gender?
df_person['Income'].groupby([df_person['Sex']]).mean()

# b. What is the mean income by gender and education?
df_person['Income'].groupby([df_person['Sex'], df_person['Education']]).mean()

# c. What is the probability of outcome == yes across gender?
df_person[(df_person['outcome'] == 'Yes')].groupby('Sex')['Sex'].count() \
    / df_person.groupby('Sex')['Sex'].count()

# verify
len(df_person.loc
    [(df_person['outcome'] == 'Yes') & (df_person['Sex'] == 'Female')])
len(df_person.loc[
    (df_person['outcome'] == 'Yes') & (df_person['Sex'] == 'Male')])

df_person.groupby('Sex')['Sex'].count()
