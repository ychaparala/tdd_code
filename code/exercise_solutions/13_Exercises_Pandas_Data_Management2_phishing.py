###########################################
# File: 06_Exercises_Pandas_Data_Management.py
# Created: July 15, 2018
# Last Modified: July 20, 2018
# Author: Ra Inta and Evan Carey, written for BH Analytics, LLC
###########################################

###########################################
### Part II of Data Management       ######
###########################################

## 1) Continue the script you developed in the prior exercise, where you already imported
## this data.

## 2) Check the dtypes each variable in each of the three tables, and modify it if you need
## to.
## a. Inspect each dtype
campaign_df.dtypes

## CampaignID       int64
## CampaignType    object
## DateTimeSent    object
## dtype: object

# Note: the objects here are categories or dates.

lookup_df.dtypes

## LookupID                  int64
## UserID                    int64
## CampaignID                int64
## TimeOpened               object
## TimeClickedLink          object
## TimeSubmitted            object
## TimeOpenedAttachement    object
## TimeReportedSpam         object
## Browser                  object
## OnMobile                  int64
## dtype: object


user_df.dtypes

## UserID           int64
## EmailAddress    object
## FirstName       object
## LastName        object
## State           object
## Department      object
## IsManager        int64
## DateOfBirth     object
## HireDate        object
## Gender          object
## dtype: object


## b. Modify it as needed. For example, you need to convert each date to an actual
## date variable (or datetime), and you need to convert Gender to be
## categorical.

user_df["Gender"] = user_df["Gender"].astype('category')

# You should always check the result of data transformations:
user_df["Gender"].dtype
user_df["Gender"].unique()
user_df["Gender"].value_counts()

# Convert datetime vars
campaign_df["DateTimeSent_dt"] = \
    pd.to_datetime(campaign_df["DateTimeSent"])
# Note: if you are able to anticipate this earlier, you can capture
# specific columns as datetime series upon import:
# campaign_df = pd.read_csv("data/phishing/Campaign.csv" \
#                           parse_dates=[2], \
#                           keep_date_col=True, \
#                           infer_datetime_format=True)

user_df["DateOfBirth_dt"] = \
    pd.to_datetime(user_df["DateOfBirth"])
user_df["HireDate_dt"] = \
    pd.to_datetime(user_df["HireDate"])

## c. For each string variable, do you want to turn it into a category? Why or why
## not?

# Deciding on what should be a category often depends on what you plan to do
# with the data. The various ID keys of the datasets (CampaignID, LookupID and
# UserID) could be categories, to protect them from accidental math or string
# operations. It is important to be consistent with your choice here!

# For the Campaign data, the CampaignType should be a category.
# For Lookup: Browser and OnMobile should be categorical.
# For User: State, Department and IsManager should be categorical.
# We'll also convert the various IDs, but that is optional.

# This is a good use of your time!! 
# You are getting to know your data, and thinking about each element.
# What information does each column represent? 

# Campaign Table
campaign_df["CampaignType"] = \
    campaign_df["CampaignType"]\
    .astype('category')
campaign_df["CampaignID"] = \
    campaign_df["CampaignID"]\
    .astype('category')
# Lookup Table
lookup_df["LookupID"] = \
    lookup_df["LookupID"]\
    .astype('category')
lookup_df["UserID"] = \
    lookup_df["UserID"]\
    .astype('category')
lookup_df["CampaignID"] = \
    lookup_df["CampaignID"]\
    .astype('category')
lookup_df["Browser"] = \
    lookup_df["Browser"]\
    .astype('category')
lookup_df["OnMobile"] = \
    lookup_df["OnMobile"]\
    .astype('category')
# User table
user_df["UserID"] = \
    user_df["UserID"]\
    .astype('category')
user_df["State"] = \
    user_df["State"]\
    .astype('category')
user_df["Department"] = \
    user_df["Department"]\
    .astype('category')
user_df["IsManager"] = \
    user_df["IsManager"]\
    .astype('category')

## d. Calculate a new column in the user table, age as of 1/1/2018. You can use
## code like this:
## # Calculate age in years as of 2015-01-01
## df_1['Age_years'] = \
## ((pd.to_datetime('2015-01-01') - df_1['DateOfBirth']).dt.days/365.25)

user_df['Age_years'] = \
    (pd.to_datetime('2018-01-01') - user_df['DateOfBirth_dt']).dt.days/365.25
# Note the use of broadcasting: pd.to_datetime('2018-01-01') is a constant,
# while user_df['DateOfBirth_dt'] is a series (vector)

## e. For the campaign table, we want to identify campaigns that were sent early
## in the morning versus later in the afternoon. Perhaps people are more
## susceptible to phishing attacks later in the day? To support this analysis, we
## need to create a new variable that is ‘time of day’. You can use string
## formatting on the DateTimeSent to identify the time of day sent. Save this as
## a new variable

campaign_df['TimeOfDay'] = \
    campaign_df['DateTimeSent_dt']\
    .dt.hour

## f. Now discretize this variable into ‘before 12 (noon)’ and ‘after 12 (noon)’, and
## save that as a new variable.

# Once again, there are a few ways you could do this. Here is a list
# comprehension, for a relatively compact expression:
campaign_df['CampaignSentMorningAfternoon'] = \
    ['afternoon' if x >= 12 else 'morning' for x in campaign_df['TimeOfDay']]
# Could also use np.where (my preference)
import numpy as np
campaign_df['CampaignSentMorningAfternoon'] = \
    np.where(campaign_df['TimeOfDay']>= 12,'afternoon','morning')


###########################################
# End of 06_Exercises_Pandas_Data_Management.py
###########################################
