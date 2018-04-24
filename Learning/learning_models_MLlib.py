#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:18:02 2018

@author: mira
"""

from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes
from pyspark.mllib.tree import DecisionTree

if __name__ == "__main__":
    
    ###########################################################################
    #########                      Spark Context                      #########
    ###########################################################################

    conf = SparkConf().\
    setAppName('sentiment-analysis').\
    setMaster('local[*]')
    
    sc = SparkContext(conf = conf)
    
    
    ###########################################################################
    #########                      Training Set                       #########
    ###########################################################################
    
    
    text_negative = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/train_negatif.csv")
    text_positive = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/train_positif.csv")
    
    train_text = text_negative.union(text_positive)
    train_labels = text_negative.map(lambda x: 0.0).union(text_positive.map(lambda x: 1.0))
    
    tf = HashingTF().transform(train_text.map(lambda x : x))
    idf = IDF().fit(tf)
    train_tfidf = idf.transform(tf)
    
    training = train_labels.zip(train_tfidf).map(lambda x: LabeledPoint(x[0], x[1]))
    #nb_cols = len(training.collect()[0].features.toArray())
    
    ##################
    # SAVE TRAINING !!
    ##################
    
    
    ###########################################################################
    #########                     Model Training                      #########
    ###########################################################################
    
    
    model_bayes = NaiveBayes.train(training)
    #save bayes_model
    model_decision_tree_entropy = DecisionTree.trainClassifier(training, categoricalFeaturesInfo={}, impurity="entropy", maxDepth=5, numClasses=2)
    #save TR_entropy_model
    model_decision_tree_gini = DecisionTree.trainClassifier(training, categoricalFeaturesInfo={}, impurity="gini", maxDepth=5, numClasses=2)
    #save TR_gini_model
    
    ###########################################################################
    #########                     Model Testing                       #########
    ###########################################################################
    
    test_text = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test.csv")
    
    tf_test = HashingTF().transform(test_text.map(lambda x : x))
    idf_test = IDF().fit(tf_test)
    tfidf_test = idf_test.transform(tf_test)
    
    ##################
    # SAVE TEST !!
    ##################
    
    #Bayes
    predictions_bayes = model_bayes.predict(tfidf_test)
    num_pos_bayes = predictions_bayes.countByValue()[1.0]
    num_neg_bayes = predictions_bayes.countByValue()[0.0]
    
    print("========== PREDICTION : ==========")
    print("- Positif : " , num_pos_bayes)
    print("- Negatif : " , num_neg_bayes)
    
    #decision tree entropy
    predictions_decision_tree_enptropy = model_decision_tree_entropy.predict(tfidf_test)
    num_pos_entropy = predictions_decision_tree_enptropy.countByValue()[0.0]
    num_neg_entropy = predictions_decision_tree_enptropy.countByValue()[1.0]
    
    #decision tree gini
    print("========== PREDICTION : ==========")
    print("- Positif : " , num_pos_entropy)
    print("- Negatif : " , num_neg_entropy)
    
    predictions_decision_tree_gini = model_decision_tree_gini.predict(tfidf_test)
    num_pos_gini = predictions_decision_tree_gini.countByValue()[0.0]
    num_neg_gini = predictions_decision_tree_gini.countByValue()[1.0]
    
    print("========== PREDICTION : ==========")
    print("- Positif : " , num_pos_gini)
    print("- Negatif : " , num_neg_gini)
    
    
    
    
    
    
    
    
    
    
    