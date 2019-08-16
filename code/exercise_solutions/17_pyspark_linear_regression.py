#!/usr/bin/env python
#
###########################################
#
# File: pyspark_linear_regression.py
# Author: Evan Carey and Ra Inta
# Description:
# Created: May 22, 2019
# Last Modified: May 22, 2019
#
###########################################


import os
import numpy as np

from pyspark.sql import SparkSession

from pyspark.ml.regression import LinearRegression
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit, CrossValidator


# 1)	Import and describe the dataset univariately (what is the mean, median, min, max, etc for each variable).
spark = SparkSession.builder.appName('sparkLinearRegression').getOrCreate()

data_file = os.path.join("data", "manufacturing", "power_plant", "power_plant.csv")


power_df = spark.read.csv(data_file, inferSchema=True, header=True)

##################################################


# 2)	We will focus on predicting power output (PE). What is your best
# estimate of PE in the absence of any other information (just the power column)?
#     a.	Calculate the sample mean


power_df.select("PE").describe().show()

# mean(PE) = 454.365


#     b.	Fit a linear regression with only an intercept, then summarize the result


linReg = LinearRegression(maxIter=10, regParam=0.2, elasticNetParam=0.1)

#     c.	Write out the regression equation you just fit and plug in the parameter estimate from the model.
#
# 3)	Now consider the pairwise relationships between each individual predictor (AT, AP, RH and V) and the corresponding outcome of PE.
#     a.	For each predictor, calculate the Pearson correlation coefficient
#     between it and the target variable, PE. Does any variable appear
#     significant?

power_df.corr("PE", "AT")
power_df.corr("PE", "AP")
power_df.corr("PE", "RH")
power_df.corr("PE", "V")

#     b.	For each predictor, find the corresponding p-value.
#
#
# 4)	We may also need to understand if our predictors are related to each other.

#     a.	For each possibly pairwise combination of the predictors, create a scatterplot and find the correlation between the predictors. Are any of them related to each other?


power_df.corr("AT", "AP")
power_df.corr("AT", "RH")
power_df.corr("AT", "V")

power_df.corr("AP", "RH")
power_df.corr("AP", "V")

power_df.corr("RH", "V")

# 5)	For the final step in this modeling process, we will fit a multivariate linear regression using (potentially) all of the predictors.
#     a.	For each predictor, consider if you need a non-linear fit. You may
#     'cheat' here, and produce a scatterplot matrix in seaborn (sns.pairplot),
#     as the data will fit in memory. In practice this will be harder for big
#     data sets.

import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(power_df.toPandas())
plt.show()


# Re-label some columns, set aside some validation data, construct a pipeline
power_df = power_df.withColumnRenamed(power_df.columns[-1], "label")

power_feature_labels = power_df.columns[0:4]

# Save this to be used in the pipeline
power_feature_vector = VectorAssembler(
 inputCols=power_feature_labels,
 outputCol="features")


power_train, power_test = power_df.randomSplit([0.75, 0.25], 42)

print("\nRows of data for training: {}; testing: {}".format(power_train.count(), power_test.count()))

linReg = LinearRegression()

# Just for this exercise, we'll generate two pipelines:
# One for data processing for ingestion, the other including the
# regression step.

processing_pipeline = Pipeline(stages=[power_feature_vector])
lin_pipeline = Pipeline(stages=[power_feature_vector, linReg])

linRegModel = lin_pipeline.fit(power_train)

print(f"Coefficients: {linRegModel.stages[-1].coefficients}")
print(f"Intercept: {linRegModel.stages[-1].intercept}")

# How many features are there?

print("\nNumber of model features: {}".format(linRegModel.stages[-1].numFeatures))

# Summarize the results and validate
trainingSummary = linRegModel.stages[-1].summary
print(f"numIterations: {trainingSummary.totalIterations}")
print(f"objectiveHistory: {trainingSummary.objectiveHistory}")

trainingSummary.residuals.show(10)
print(f"RMSE: {trainingSummary.rootMeanSquaredError}")
print(f"r2: {trainingSummary.r2}")

power_test = power_feature_vector.transform(power_test)
validation = linRegModel.stages[-1].transform(power_test).select("prediction", "label")
evaluator = RegressionEvaluator()

print(f"\nRMSE: {evaluator.evaluate(validation)}\n" )

#     b.	Construct a final ‘best’ model using the linear (or non-linear)
#     terms you decided on above.
#     c.	Use this final model to summarize the relationships between the
#     predictors and the outcome. Summarize these results verbally.

##################################################


##################################################
from pyspark.ml.regression import GeneralizedLinearRegression

glr = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=10, regParam=0.3)
glr_pipeline = Pipeline(stages=[power_feature_vector, glr])

# Fit the model
model = glr_pipeline.fit(power_train)

##################################################
# ## Hyperparameter Tuning
# ### Single Validation Split

paramGrid = ParamGridBuilder()\
    .addGrid(linReg.regParam, [0.1, 0.01, 5.0])\
    .addGrid(linReg.elasticNetParam, np.arange(0.0, 1.25, 0.25))\
    .addGrid(linReg.fitIntercept, [False, True])\
    .build()


# Then we will split off 25% of the training data to a single validation set. We'll make use of the `linReg` linear regressor and `RegressionEvaluator` we created above (which has an RMSE default output metric):

trainValSplit = TrainValidationSplit(estimator=linReg,
 estimatorParamMaps=paramGrid,
 evaluator=RegressionEvaluator(),
 trainRatio=0.75)


# We can then fit the best model, according to the evaluator, by exploring the hyperparameter grid:

power_train = power_feature_vector.transform(power_train)

linReg_tvs = trainValSplit.fit(power_train)


linReg_tvs.transform(power_test).select("features", "label", "prediction").show(10)


# The default `RegressionEvaluator` requires a `prediction` and a `label` column:


linReg_valid = linReg_tvs.transform(power_test).select("prediction", "label")
evaluator = RegressionEvaluator()

print(f"\nRMSE: {evaluator.evaluate(linReg_valid)}\n" )


# What coefficients were chosen?

print(f"Model coefficients: {linReg_tvs.bestModel.coefficients}")
print(f"Model intercept: {linReg_tvs.bestModel.intercept}")


# Accessing the actual hyperparameters is currently an arcane process -- we have to query the underlying Java object:


print(f"Chosen regularization parameter: {linReg_tvs.bestModel._java_obj.getRegParam()}")
print(f"Chosen elastic net parameter: {linReg_tvs.bestModel._java_obj.getElasticNetParam()}")

# Both values are very close to zero; no need for penalized linear regression


###########################################
# End of linear_regression.py
###########################################
