#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:18:02 2018

@author: mira
"""

from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree

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
    
    test_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/test_clean.csv"
    test = test_set(test_file, idf)
    
    print("\nDone : Tf-IDF training and test sets")
    
    
    ###########################################################################
    #########                     Model Training                      #########
    
    print("\n=================== Training ================== \n")
    
    
    model_decision_tree_entropy = DecisionTree.trainClassifier(training, categoricalFeaturesInfo={}, impurity="entropy", maxDepth=5, numClasses=2)
    print("Done : DT entropy training")
    

    ###########################################################################
    #########                     Model Testing                       #########
    
    
    print("\n=================== Testing =================== \n")
    
    #decision tree entropy
    predictions_decision_tree_enptropy = model_decision_tree_entropy.predict(test)
    num_pos_entropy = predictions_decision_tree_enptropy.countByValue()[1.0]
    num_neg_entropy = predictions_decision_tree_enptropy.countByValue()[0.0]
    
    #decision tree gini
    print("\n== PREDICTION ENTROPY : ==\n")
    print("- Positive : " , num_pos_entropy)
    print("- Negative : " , num_neg_entropy)
    
    file.write("\n\n" + "================ DECISION TREE (entropy) ============== " + "\n\n")
    file.write("- Positive : " + str(num_pos_entropy) + "\n")
    file.write("- Negative : " + str(num_neg_entropy) + "\n")
    
    
    
    ###########################################################################
    #########           Testing on Brexit Labeled Data                #########
    
    
    print("\n========= Test on Brexit labeled data ========= ")
    
    text_negative_brexit = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/brexit_negatif_clean.csv")
    text_positive_brexit = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/brexit_positif_clean.csv")

    test_text_brexit = text_negative_brexit.union(text_positive_brexit)
    test_tlabels_brexit = text_negative_brexit.map(lambda x: 0.0).union(text_positive_brexit.map(lambda x: 1.0))
    
    tf_test_brexit = HashingTF(numFeatures=10000).transform(test_text_brexit.map(lambda x : x))
    
    tfidf_test_brexit = idf.transform(tf_test_brexit)
    
    #decision tree entropy
    labeled_prediction_entropy = test_tlabels_brexit.zip(model_decision_tree_entropy.predict(tfidf_test_brexit)).map(lambda x: {"actual": x[0], "predicted": x[1]})
    accuracy_entropy = 1.0 * labeled_prediction_entropy.filter(lambda doc: doc["actual"] == doc['predicted']).count() / labeled_prediction_entropy.count()
    
    
    print('\n== ACCURACY DT ENTROPY : ', accuracy_entropy , '==')
    
    file.write("\n" + "== Results on labeled data (Brexit) ==" + "\n")
    file.write('\n-> ACCURACY DT ENTROPY : ' + str(accuracy_entropy) + '\n')
    
    
    
    
    
    