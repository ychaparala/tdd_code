#!/usr/bin/env python
#
###########################################
#
# File: data_management_spark_faults.py
# Authors: Evan Carey and Ra Inta
#
# Description: Data Management using PySpark
# This uses a modified dataset based on finding
# faults in various experiments on stell manufacture.
# Created: May 21, 2019
# Last Modified: May 21, 2019
#
###########################################


import os

from pyspark.sql import SparkSession
import pyspark.sql.functions as s_f

spark = SparkSession.builder.appName('sparkDataManagement').getOrCreate()

data_dir = os.path.join("data", "manufacturing", "faults")

feature_data_file = os.path.join(data_dir, "faults_features.csv")
label_data_file = os.path.join(data_dir, "faults_labels.csv")

feature_names_file = os.path.join(data_dir, "names_features.txt")
label_names_file = os.path.join(data_dir, "names_labels.txt")

feature_df = spark.read.csv(feature_data_file, inferSchema=True)
label_df = spark.read.csv(label_data_file, inferSchema=True)

feature_names = spark.read.text(feature_names_file)
label_names = spark.read.text(label_names_file)

# Acquire column names from files
# Renaming whole DataFrames is annoying because they are immutable

feature_names_list = [x[0] for x in feature_names.collect()]
feature_df = feature_df.toDF(*feature_names_list)  # Note the '*' here to unroll the list as arguments

label_names_list = [x[0] for x in label_names.collect()]
label_df = label_df.toDF(*label_names_list)  # Note the '*' here to unroll the list as arguments


# Join on ID
faults_df = feature_df.join(label_df, on="ID", how="left")

### Basic DataFrame manipulations
# Check shape
faults_df.count()
len(faults_df.columns)

# Print schema
faults_df.printSchema()

# Display first 5 rows
faults_df.show(5)

# Get numerical summary
faults_df.describe().show()

# Select X_minimum only
faults_df.select("X_Minimum").describe().show()

# +-------+-----------------+
# |summary|        X_Minimum|
# +-------+-----------------+
# |  count|             1941|
# |   mean|571.1360123647604|
# | stddev| 520.690671421655|
# |    min|                0|
# |    max|             1705|
# +-------+-----------------+


# Rename first column
faults_df = faults_df.withColumnRenamed('X_Minimum', 'x_min')

## Sort Data
faults_df.sort(faults_df["x_min"]).show(5)
faults_df.sort(faults_df["x_min"].desc()).show(5)

## Subset data
faults_df.filter(faults_df["x_min"] > 1000).show(3)
faults_df.filter(faults_df["x_min"] > 1000).count()
faults_df.filter(faults_df["x_min"] > 1000).describe("x_min").show()

faults_df.select('*').show(3) # Select All Columns

### Data cleaning
## Fix "Other_Faults": the 'unlikely' level should be 0
faults_df.select('Other_Faults').distinct().show()
faults_df.groupBy('Other_Faults').count().show()

faults_df = faults_df.withColumn('Other_Faults',
                     s_f.when(faults_df['Other_Faults'] != 'Unlikely', faults_df['Other_Faults']).otherwise(0))

faults_df.select('Other_Faults').distinct().show()

# Now make it an int like the others
faults_df = faults_df.withColumn("Other_Faults",
                                 faults_df["Other_Faults"].cast("int"))


## Dealing with missing data
faults_df.count()
faults_df.dropna().count()

# Turns out "Pastry" has some missing values:
faults_df.select("Pastry").count()
faults_df.select("Pastry").dropna().count()

# These can be set to zero:
faults_df = faults_df.fillna(0)

faults_df.count()
faults_df.dropna().count()

# Transform the 'Other_Faults' column to show the logical inverse and rename it
faults_df = faults_df.withColumn('named_faults', 1 - faults_df['Other_Faults'])


### Group-by and univariate and bivariate analysis
faults_df.groupBy('named_faults').count().show()

#### Univariate Descriptions
faults_df.select('named_faults', 'Other_Faults').distinct().show()

## Quantiles
faults_df.select("x_min").dropna().approxQuantile("x_min", [0.5], 0)
faults_df.select("x_min").dropna().approxQuantile("x_min", [0.25, 0.5, 0.75], 0)
faults_df.select("x_min").describe().show()

#### Bivariate Summaries
faults_df.corr("x_min", "X_Maximum") # Pearson correlation coef

faults_df.corr("x_min","Y_Minimum")
faults_df.corr("x_min","Other_Faults")

faults_df.cov("named_faults", "Other_Faults") # Covariance

## Cross tabs
faults_df.crosstab("named_faults", "Other_Faults").show()

## Groupby Summaries
faults_df.groupBy("named_faults").count().show()

faults_df.groupBy('named_faults').avg('x_min').show()
faults_df.groupBy('Pastry').avg('x_min').show()

faults_df.groupBy('named_faults', 'Pastry').avg('x_min').show()

## Pivot results

faults_df\
    .dropna(subset='Pastry')\
    .groupBy('named_faults')\
    .pivot('Pastry')\
    .avg('x_min')\
    .show()

## Split Data Into Random Subsets
faults_df_train, faults_df_test = \
    faults_df.randomSplit([0.6, 0.4], 20)

## Get 10% sample
faults_df.sample(0.2).select("x_min", "Pastry", "named_faults").show()


### Exporting to other formats
## Convert to Pandas DataFrame
## This brings full data into memory on driver, only do
## with smaller datasets (like results you want to plot...)
faults_pd = faults_df.toPandas()


#### Persistent Objects
## Save to parquet file
output_parquet_file = os.path.join(data_dir, "faults_data_management.parquet")
faults_df.write.parquet(output_parquet_file, mode='overwrite')


spark.stop()

###########################################
# End of data_management_spark_faults.py
###########################################
