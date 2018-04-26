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


def training_set(pos_file, neg_file):
    text_negative = sc.textFile(neg_file)
    text_positive = sc.textFile(pos_file)
    
    train_text = text_negative.union(text_positive)
    train_labels = text_negative.map(lambda x: 0.0).union(text_positive.map(lambda x: 1.0))
    
    tf = HashingTF(numFeatures=10000).transform(train_text.map(lambda x : x))
    idf = IDF().fit(tf)
    train_tfidf = idf.transform(tf)
    
    training = train_labels.zip(train_tfidf).map(lambda x: LabeledPoint(x[0], x[1]))
    return (training, idf)


def test_set(test_file, idf):
    test_text = sc.textFile(test_file)
    
    tf_test = HashingTF(numFeatures=10000).transform(test_text.map(lambda x : x))
    tfidf_test = idf.transform(tf_test)
    return tfidf_test


if __name__ == "__main__" :
    
    
    ###########################################################################
    #########                      Spark Context                      #########
    
    conf = SparkConf().\
    setAppName('sentiment-analysis').\
    setMaster('local[*]')
    
    sc = SparkContext(conf = conf)
    
    file = open("resultat_learning.txt","a")
    file.write("\n\n\n\n*******************************************************\n")
    
    
    ###########################################################################
    #########                 Training and Test Set                   #########
    
    pos_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/training_positif_clean.csv"
    neg_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/training_negatif_clean.csv"
    
    training_idf = training_set(pos_file, neg_file)
    training = training_idf[0]
    idf = training_idf[1]
    
    test_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/test_clean" + ".csv"
    test = test_set(test_file, idf)
    
    print("\nDone : Tf-IDF training and test sets")
    
    
    ###########################################################################
    #########                      Model Training                     #########
    
    model_bayes = NaiveBayes.train(training)
    print("Done : Bayes training ")


    ###########################################################################
    #########                     Model Testing                       #########
    
    
    #Bayes
    predictions_bayes = model_bayes.predict(test)
    num_pos_bayes = predictions_bayes.countByValue()[1.0]
    num_neg_bayes = predictions_bayes.countByValue()[0.0]
    
    print("\n== PREDICTION BAYES : ==\n")
    print("- Positive : " , num_pos_bayes)
    print("- Negative : " , num_neg_bayes)
    
    file.write("\n\n" + "======================== BAYES ======================== " + "\n\n")
    file.write("- Positive : " + str(num_pos_bayes) + "\n")
    file.write("- Negative : " + str(num_neg_bayes) + "\n")
    
    
    
    ###########################################################################
    #########           Testing on Brexit Labeled Data                #########
    
    
    print("\n========= Test on Brexit labeled data ========= ")
    
    text_negative_brexit = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/brexit_negatif_clean.csv")
    text_positive_brexit = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/brexit_positif_clean.csv")

    test_text_brexit = text_negative_brexit.union(text_positive_brexit)
    test_tlabels_brexit = text_negative_brexit.map(lambda x: 0.0).union(text_positive_brexit.map(lambda x: 1.0))
    
    tf_test_brexit = HashingTF(numFeatures=10000).transform(test_text_brexit.map(lambda x : x))
    
    tfidf_test_brexit = idf.transform(tf_test_brexit)
    
    #prediction and evaluation
    labeled_prediction_bayes = test_tlabels_brexit.zip(model_bayes.predict(tfidf_test_brexit)).map(lambda x: {"actual": x[0], "predicted": x[1]})
    accuracy_bayes = 1.0 * labeled_prediction_bayes.filter(lambda doc: doc["actual"] == doc['predicted']).count() / labeled_prediction_bayes.count()

    
    print('\n== ACCURACY BAYES : ', accuracy_bayes , '==')
    
    file.write("\n" + "== Results on labeled data (Brexit) ==" + "\n")
    file.write('\n-> ACCURACY BAYES : ' + str(accuracy_bayes) + '\n')
    
    
    
