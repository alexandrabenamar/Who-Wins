#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyspark.mllib.classification import LogisticRegressionWithSGD
from functions_MLlib import spark_context, training_set, test_set, write_result, brexit_labeled_data, mode_predict


if __name__ == "__main__" :
    
    sc = spark_context()
    
    numFeatures = 10000
    
    print("Training...\n")
    
    (training, idf) = training_set(sc, numFeatures = numFeatures)
    model = LogisticRegressionWithSGD.train(training)
    
    print("Test... \n")
    
#    test = test_set(sc, numFeatures = numFeatures, idf = idf)
#    (num_pos, num_neg) = mode_predict(model, test)
    
    print("Test on Brexit labeled data...\n")
    
    (accuracy, f1) = brexit_labeled_data(sc, model = model, numFeatures = numFeatures, idf = idf)

    print("Saving results...")
    
    write_result(1, 1, accuracy = accuracy, f1 = f1, name = "Logistic Reg")
    
    
