#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 23:41:07 2018

@author: mira
"""
from pyspark.ml.classification import LinearSVC
from functions_ml import spark_context, training_set, test_set, write_result, brexit_labeled_data, model_predict


def SVC_train(training):
    
    trainer_SVC = LinearSVC(maxIter=10, regParam=0.1)
    model = trainer_SVC.fit(rescaledData)
    
    return model

if __name__ == "__main__":

    numFeatures = 10000
    
    sc = spark_context()
    
    print("Training...\n")
    
    (rescaledData, idfModel) = training_set(sc = sc, numFeatures = numFeatures)
    print(33333333333333333333333333333333333333333333)

    model = SVC_train(training = rescaledData)

    print("Test... \n")

#    rescaled_test_df = test_set(sc, numFeatures = numFeatures, idfModel = idfModel)
#    (num_pos, num_neg) = model_predict(model, rescaled_test_df)
    
    print("Test on Brexit labeled data...\n")
    
    (accuracy, f1) = brexit_labeled_data(sc = sc, numFeatures = numFeatures, idfModel = idfModel , model = model)
   
    print("Saving results...\n")
    
    write_result(1, 1, accuracy = accuracy, f1 = f1, name = "Neural Network")
    
    