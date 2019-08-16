###########################################
#
# File: 07_Exercises_Pandas_Data_Management.py
# Created: July 17, 2018
# Last Modified: July 16, 2018
# Author: Ra Inta and Evan Carey, written for BH Analytics, LLC
###########################################

## 1) Continue the script you developed in the prior exercises.
## 2) Missing Data:
## a. Check each of the three tables for missing data. Do any of the tables have any
## missing data? Which columns have missing data?

# Check for missing data:
print(campaign_df.isnull().sum())
print(lookup_df.isnull().sum())
print(user_df.isnull().sum())


# The only fields with missing data were from lookup_df:
#
# Field name            Number of missing values
#-----------------------------------------------
#LookupID                     0
#UserID                       0
#CampaignID                   0
#TimeOpened                1214
#TimeClickedLink          22565
#TimeSubmitted            23596
#TimeOpenedAttachement    23004
#TimeReportedSpam         19887
#Browser                  21018
#OnMobile                     0

# Have a look at range and potential univariate outliers:
campaign_df.describe()
lookup_df.describe()
user_df.describe()


## 3) Our goal is to combine these three files into a single file we can use for analysis.

## b. To do this, we need to merge date from all three files into a single file. You
## will need to think carefully about what steps to take to create this final
## analytic file. You will need to do multiple subsets, merges, and create new
## variables. The final file should have a row for every User and campaign
## combination, with the following columns:
## i. UserID
## ii. CampaignID
## iii. CampaignType
## iv. CampaignSentMorningAfternoon (if campaign was sent in morning or
## afternoon)
## v. UserAge (User Age as of 2018-01-01)
## vi. UserTenure (User tenure at company as of 2018-01-01, how long
## have they worked here?)
## vii. UserOpenedEmail (Did the user open the email? Yes or no)
## viii. UserFail (Did the user fail by either clicking the link, Submitted info,
## or Opening the attachment? Should be values of ‘Yes’ and ‘No’)
## ix. UserReportedSpam (Did the user report the email as spam?)


# Merge data to determine efficacy of phishing campaign.
# Check the column names of each dataframe to determine common keys to join by:
merged_df = pd.merge(lookup_df,
                     user_df,
                     how='left',
                     left_on='UserID',
                     right_on='UserID')
# Strange error message given here in Pandas < 0.23, you can ignore if you see it. 
# Note: we could have used "on='UserID'" here, because the indices are the same
# for the left- and right- hand dataframes. However, it can be clearer to specify the
# full syntax. Also if they were named differently you would need to specify them this way. 

merged_df2 = pd.merge(merged_df,
                     campaign_df,
                     how='left',
                     left_on='CampaignID',
                     right_on='CampaignID')

# create userfail column
merged_df['UserFail'] = \
    np.where(merged_df['TimeClickedLink'].notnull() | 
            merged_df['TimeSubmitted'].notnull() | 
            merged_df['TimeOpenedAttachement'].notnull(),
            True,False)
# check distribution
# Overall 'failure' rate (success of phishing campaign):
merged_df['UserFail'].sum()*100.0/len(merged_df)  # Around 11.8%

# The logic of the following is a little tricky!
merged_df['UserOpenedEmail'] = \
    np.where(merged_df['TimeOpened'].notnull(),
             'yes','no')
# Roughly: "If x is not null, then 'yes'"

# Once again, you should check that your transforms applied how you expect them
# to:
merged_df.loc[merged_df['TimeOpened'].notnull(),
              ['UserOpenedEmail', 'TimeOpened']].sample(n=10)  # You should see 'yes' corresponding to timeOpened not null
merged_df.loc[merged_df['TimeOpened'].isnull(),
              ['UserOpenedEmail', 'TimeOpened']].sample(n=10)  # You should see 'no' corresponding to NaN

# Similarly:
merged_df['UserReportedSpam'] = \
    np.where(merged_df['TimeReportedSpam'].notnull(),
             'yes','no')
# Once again, you should check that your transforms applied how you expect them
# to:
merged_df.loc[merged_df['TimeReportedSpam'].notnull(),
              ['UserReportedSpam', 'TimeReportedSpam']].sample(n=10)  # You should see 'yes' corresponding to TimeReportedSpam not null
merged_df.loc[merged_df['TimeOpened'].isnull(),
              ['UserReportedSpam', 'TimeReportedSpam']].sample(n=10)  # You should see 'no' corresponding to NaN

## create user tenure (in years)
merged_df['UserTenure'] = \
    (pd.to_datetime('2018-01-01') - merged_df['HireDate_dt']).dt.days/365.25

## Merge in the campaign data
merged_2 = \
    pd.merge(merged_df,
             campaign_df[['CampaignID', 'CampaignType', 'CampaignSentMorningAfternoon']],
             how='left',
             on='CampaignID')

## Create dataframe with only the colums of interest
df_analytic = \
    merged_2[['UserID', 'CampaignID', 'Browser',
       'OnMobile', 'IsManager', 'Gender', 'Age_years', 'UserFail',
       'UserOpenedEmail', 'UserReportedSpam', 'UserTenure', 'CampaignType',
       'CampaignSentMorningAfternoon']]
df_analytic


###########################################
# File: 07_Exercises_Pandas_Data_Management.py
###########################################
