##################################################################################################################
## File: Import and EDA - Healthcare Solution
## Author: Evan Carey, written for BH Analytics
## Date Created: 2018-07-21
## Last date modified: 2019-07-08
##################################################################################################################


## import modules
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys


os.getcwd()  # See your current working directory
os.chdir("path/to/your/directory")
# os.chdir(r"C:\Users\evancarey\Dropbox\Work")
os.getcwd()  # Check you're in the right place

#### Import OutpatientVisit File and perform EDA / Data Cleaning ####
## import the  patient file (after checking it with a text editor first!)
df_outpatientVisit = pd.read_csv('Data/Data_Sims/healthcare/OutpatientVisit.csv')

## inspect the dataframe
df_outpatientVisit.head()
df_outpatientVisit.tail()
## Dimensionality and dtypes
df_outpatientVisit.shape
df_outpatientVisit.dtypes
## basic summaries 
df_outpatientVisit.describe()  
df_outpatientVisit\
    .select_dtypes(include=['O'])\
    .describe()

## change visitdate to a date object
df_outpatientVisit['VisitDate_dt'] = pd.to_datetime(df_outpatientVisit['VisitDate'])
df_outpatientVisit.loc[:,['VisitDate_dt','VisitDate']]
df_outpatientVisit['VisitDate_dt'].describe()

## explore date distribution visually with histogram
df_outpatientVisit['VisitDate_dt'].hist(bins=100)

## Examine the file...is it 'long' or 'wide'?
## Wide for ICD Codes
df_outpatientVisit.loc[:,['ICD10_1','ICD10_2', 'ICD10_3']]

## Long for Clinic codes and patientIDs
df_outpatientVisit.loc[:,['PatientID', 'ClinicCode']]

## What is the min, max, and mean number of visits per patient?
patient_visits = \
    df_outpatientVisit\
    .groupby('PatientID')\
    .count()['VisitID']
patient_visits.describe()

## How many patients have only one visit? 
(patient_visits == 1).sum() 
## What percent of patients have only one visit? 
(patient_visits == 1).sum() / patient_visits.count()
## How many patients have more than 30 visits?
(patient_visits > 30).sum()
## What percent?
(patient_visits > 30).sum() / patient_visits.count()

#### Import and Merge in the clinic codes ####
## import the  patient file (after checking it with a text editor first!)
df_clinic= pd.read_csv('Data/Data_Sims/healthcare/Clinic.csv')
## inspect the dataframe
df_clinic.head()
df_clinic.tail()
## Dimensionality and dtypes
df_clinic.shape
df_clinic.dtypes
## basic summaries 
df_clinic.describe()  
df_clinic['ClinicDescription'].value_counts(dropna=False)
## Check for missing data
df_clinic.isnull().sum(0)

## Merge clinic code to patient_visits
df_outpatientVisit2 = \
    pd.merge(df_outpatientVisit,
             df_clinic,
             how='left',
             on='ClinicCode')
## Check dimensionality
df_outpatientVisit.shape
df_outpatientVisit2.shape
## Create a dataframe with type of clinic as columns, patientID as row, and number of visits as the values
df_clin_vis_long = \
    df_outpatientVisit2\
    .groupby(['PatientID','ClinicDescription'])['VisitID']\
    .count()
## Unstack this long result
df_clin_vis_long.unstack(level='ClinicDescription')
## Finish by adding in 0 for any of the missing:
df_clin_vis_wide = \
    df_clin_vis_long\
    .unstack(level='ClinicDescription')\
    .fillna(0)
## What is the mean number of primary care visits per patient?
df_clin_vis_wide['Primary Care'].describe() 


#### Import and Merge Disease Codes ####
df_diseasemap = pd.read_csv('Data/Data_Sims/healthcare/DiseaseMap.csv')
## inspect the dataframe
df_diseasemap.head()
df_diseasemap.tail()
## Dimensionality and dtypes
df_diseasemap.shape
df_diseasemap.dtypes
## basic summaries 
df_diseasemap.describe()  
df_diseasemap['Condition'].value_counts(dropna=False)
## Check for missing data
df_diseasemap.isnull().sum(0)

## If we want to merge to the patient ICD codes in the visit data, what do we need to do first?
## The ICD codes are in three different columns...
## We could do three different merges...or we could melt the data, then only do one join
## Subset down to patient ID and ICD codes only, then melt to long format
df_outpatientVisit_long = \
    pd.melt(df_outpatientVisit.loc[:,['PatientID','ICD10_1','ICD10_2','ICD10_3']],
            id_vars=['PatientID'],
            value_name='ICDCode',
            var_name='ICDCodeNum')
## Merge in the code to disease maps:
df_outpatientVisit_long2 = \
    pd.merge(df_outpatientVisit_long,
         df_diseasemap,
         left_on='ICDCode',
         right_on='ICD10',
         how='left')
## check output
df_outpatientVisit_long.shape
df_outpatientVisit_long2.shape
df_outpatientVisit_long2.head()
## Count the number of combinations of Conditions and PatientID
## Use the pivot_Table function - the argument for 'values' is arbitray since we are
## only counting the length
df_disease_wide = \
    df_outpatientVisit_long2\
    .pivot_table(values='ICD10',
                 columns='Condition',
                 index='PatientID',
                 aggfunc=pd.Series.count)
## Convert to zeros and ones
df_disease_wide2 = (df_disease_wide > 0).astype(int)
## What is the most common disease?
df_disease_wide2\
    .mean()\
    .sort_values()
## oddly high paralysis values! probably an error...
## Also 29% has hypertension? Maybe also an error...