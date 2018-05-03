#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.regression import LabeledPoint
from pyspark.sql.types import DoubleType
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


"""
    The file contains functions used by MLlib Supervised Learning programs
    Spark implementation of :
        Training phase
        Test phase
        Evaluation phase
"""


def spark_context():
    
    conf = SparkConf().\
    setAppName('sentiment-analysis').\
    setMaster('local[*]')
    
    sc = SparkContext(conf = conf)
    
    SparkSession.builder.getOrCreate()
        
    return sc


def training_set(sc,
                 numFeatures,
                 pos_file = "data/training_positif_clean.csv",
                 neg_file = "data/training_negatif_clean.csv"
                 ):
    """
        Input : number of retained features in the tweet-term structure
        Output : 
            normalized tweet-term format training set
            IDF model (that will be used in the test phase)
    """
    
 
    text_negative = sc.textFile(neg_file)
    text_positive = sc.textFile(pos_file)
    
    train_text = text_negative.union(text_positive)
    train_labels = text_negative.map(lambda x: 0.0).union(text_positive.map(lambda x: 1.0))
    
    tf = HashingTF(numFeatures=numFeatures).transform(train_text.map(lambda x : x))
    idf = IDF().fit(tf)
    train_tfidf = idf.transform(tf)
    
    training = train_labels.zip(train_tfidf).map(lambda x: LabeledPoint(x[0], x[1]))
    return (training, idf)


def test_set(sc,
             numFeatures,
             idf,
             test_file = "data/test_clean.csv"
             ):
    """
        Input : 
            number of retained features in the tweet-term structure
            IDF model obtained in the training phase
        Output :
            normalized tweet-term format test set 
    """
    
    test_text = sc.textFile(test_file)
    
    tf_test = HashingTF(numFeatures=numFeatures).transform(test_text.map(lambda x : x))
    tfidf_test = idf.transform(tf_test)
    
    return tfidf_test


def mode_predict(model, test_set):
    """
        Input : 
            training model obtained in the training phase
            normalized tweet-term format test set
        Output :
            prediction couple : (number of positive tweets , number of negative tweets)
    """
    
    predictions = model.predict(test_set)
    num_pos = predictions.countByValue()[1.0]
    num_neg = predictions.countByValue()[0.0]
    
    return (num_pos, num_neg)


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


def brexit_labeled_data(sc, model, numFeatures, idf):
    """
        Input : 
            training model obtained in the training phase
            number of retained features in the tweet-term structure
            IDF model obtained in the training phase
        Output :
            performance couple : (accuracy , F-measure)
    """
    
    text_negative_brexit = sc.textFile("data/brexit_negatif_clean.csv")
    text_positive_brexit = sc.textFile("data/brexit_positif_clean.csv")

    test_text_brexit = text_negative_brexit.union(text_positive_brexit)
    test_labels_brexit = text_negative_brexit.map(lambda x: 0.0).union(text_positive_brexit.map(lambda x: 1.0))
    
    tf_test_brexit = HashingTF(numFeatures=numFeatures).transform(test_text_brexit.map(lambda x : x))
    
    tfidf_test_brexit = idf.transform(tf_test_brexit)
    
    labeled_prediction = test_labels_brexit.zip(model.predict(tfidf_test_brexit)).map(lambda x: (int(x[0]), int(x[1])))
    df = labeled_prediction.toDF(["label", "prediction"])
    df = df.withColumn("label", df.label.cast(DoubleType()))
    df = df.withColumn("prediction", df.prediction.cast(DoubleType()))
    
    predictionAndLabels = df.select("label", "prediction")
    
    accuracy_evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    accuracy = accuracy_evaluator.evaluate(predictionAndLabels)
    
    f1_evaluator = MulticlassClassificationEvaluator(metricName="f1")
    f1 = f1_evaluator.evaluate(predictionAndLabels)
    
    return (accuracy, f1)















