#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyspark import SparkContext, SparkConf
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.feature import HashingTF, IDF, Tokenizer

"""
    The file contains functions used by ml Supervised Learning programs
    Spark implementation of :
        Training phase
        Test phase
        Evaluation phase
"""

def spark_context():
    
    conf = SparkConf().setAppName('sentiment-analysis').setMaster('local[*]')
    sc = SparkContext(conf = conf)
    SparkSession.builder.appName("sentiment-analysis").getOrCreate()    
        
    return sc

def training_set(sc,
                 numFeatures,
                 pos_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/training_positif_clean.csv",
                 neg_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/training_negatif_clean.csv"
                 ):
    """
        Input : 
            number of retained features in the tweet-term structure
        Output : 
            normalized tweet-term format training set
            IDF model (that will be used in the test phase)
    """
    
    text_positive = sc.textFile(pos_file)
    text_negative = sc.textFile(neg_file)
    
    pos_labels = text_positive.map(lambda x: 1.0).zip(text_positive.map(lambda x : x))
    neg_labels = text_negative.map(lambda x: 0.0).zip(text_negative.map(lambda x : x))
    
    pos_df = pos_labels.toDF(["label" , "sentence"])
    neg_df = neg_labels.toDF(["label" , "sentence"])
    
    text_df = pos_df.union(neg_df)
    
    tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
    wordsData = tokenizer.transform(text_df)
    
    hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures = numFeatures)
    featurizedData = hashingTF.transform(wordsData)
    idf = IDF(inputCol="rawFeatures", outputCol="features")
    idfModel = idf.fit(featurizedData)
    rescaledData = idfModel.transform(featurizedData)
    
    return (rescaledData, idfModel)


def test_set(sc,
             idfModel,
             numFeatures,
             test_file = "/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/test_clean.csv"
             ):
    """
        Input : 
            IDF model obtained in the training phase
            number of retained features in the tweet-term structure
        Output : 
            normalized tweet-term format test set            
    """
    
    test_text = sc.textFile(test_file)
    test_df = test_text.map(lambda x : (0,x)).toDF(["nothing" , "sentence"]) 
    
    tokenizer_test = Tokenizer(inputCol="sentence", outputCol="words")
    wordsData_test = tokenizer_test.transform(test_df)

    hashingTF_test = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=numFeatures)
    featurizedData_test = hashingTF_test.transform(wordsData_test)
    rescaledData_test = idfModel.transform(featurizedData_test)
    rescaled_test_df = rescaledData_test.select("features")    

    return rescaled_test_df


def model_predict(model, test_df):
    """
        Input : 
            training model obtained in the training phase
            normalized tweet-term format test set
        Output :
            prediction couple : (number of positive tweets , number of negative tweets)
        
    """
    
    predictions = model.transform(test_df)
    num_pos = predictions.select("prediction").rdd.map(lambda x : x["prediction"]).countByValue()[1.0]
    num_neg = predictions.select("prediction").rdd.map(lambda x : x["prediction"]).countByValue()[0.0]
    
    return(num_pos, num_neg)
    

def write_result(num_pos, num_neg, accuracy, f1, name, file = open("resultat_learning.txt","a")):
    """
        Save results in a common file
    """
    
    file.write("\n\n\n\n*******************************************************\n")
    
    file.write( "================ "+ name +" ============== " + "\n\n")
    file.write("- Positive : " + str(num_pos) + "\n")
    file.write("- Negative : " + str(num_neg) + "\n")
    
    file.write("\n" + "== Results on labeled data (Brexit) ==" + "\n")
    file.write('\n-> Accuracy '+name+' : ' + str(accuracy) + '\n')
    file.write('\n-> F_measure '+name+' : ' + str(f1) + '\n')
    
    file.close()
    

def test_with_accuracy(test_df, model):
    """
        Input :
             normalized tweet-term format test set with a "label" column
             training model obtained in the training phase
        Output : 
             performance couple : (accuracy , F-measure)
    """
    
    result = model.transform(test_df)
    
    predictionAndLabels = result.select("prediction", "label")
    accuracy_evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    accuracy = accuracy_evaluator.evaluate(predictionAndLabels)
    
    f1_evaluator = MulticlassClassificationEvaluator(metricName="f1")
    f1 = f1_evaluator.evaluate(predictionAndLabels)
    
    return (accuracy , f1)
    

def brexit_labeled_data(sc, numFeatures, idfModel, model):
    """
        Input : 
            number of retained features in the tweet-term structure
            IDF model obtained in the training phase
            training model obtained in the training phase
        Output :
            performance couple : (accuracy , F-measure)
    """
    
    brexit_positive = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/brexit_positif_clean.csv")
    brexit_negative = sc.textFile("/home/mira/TAF/projet_BDD/code_BDD/test_petit_jeu_de_donnees/data/brexit_negatif_clean.csv")
    
    pos_labels_brexit = brexit_positive.map(lambda x : 1.0).zip(brexit_positive.map(lambda x : x))
    neg_labels_brexit = brexit_negative.map(lambda x : 0.0).zip(brexit_negative.map(lambda x : x))
    
    pos_df_brexit = pos_labels_brexit.toDF(["label" , "sentence"])
    neg_df_brexit = neg_labels_brexit.toDF(["label" , "sentence"])
    test_df_brexit = pos_df_brexit.union(neg_df_brexit)
    
    tokenizer_test_brexit = Tokenizer(inputCol="sentence", outputCol="words")
    wordsData_test_brexit = tokenizer_test_brexit.transform(test_df_brexit)
    hashingTF_test_brexit = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=numFeatures)
    featurizedData_test_brexit = hashingTF_test_brexit.transform(wordsData_test_brexit)
    rescaledData_test_brexit = idfModel.transform(featurizedData_test_brexit)
    rescaled_test_df_brexit = rescaledData_test_brexit.select("features" , "label")
    
    (accuracy, f1) = test_with_accuracy(rescaled_test_df_brexit, model)
    
    return (accuracy, f1)










