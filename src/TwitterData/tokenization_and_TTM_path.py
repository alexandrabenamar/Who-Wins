#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk import word_tokenize
from scipy.sparse import csr_matrix
from operator import itemgetter
import pandas as pd
import csv


def tokenize_unigram (path):
    """
        Generate uni-gram tokenization
        # Input : cleansed csv document path
        # Output : list of tokenized tweets
    """
    

    tweets = []
    
    count=0
    Reader = csv.reader(open(path), delimiter=';')
    for row in Reader:
        if (count ==0):
            indx = row.index("text")
        else:
            tweets.append(word_tokenize(row[indx]))
        count = count +1
    
    return tweets
    

def tokenize_bigram (path):
    """
        Generate bi-gram tokenization
        # Input : cleansed csv document path
        # Output : list  of bi-gram tokenized tweets
    """
    
    tweets = []
    
    count=0
    Reader = csv.reader(open(path), delimiter=';')
    for row in Reader:
        if (count ==0):
            indx = row.index("text")
        else:
            unigram = word_tokenize(row[indx])
            tweet = []
            for i in range(len(unigram)-1) :
                tweet.append( (unigram[i],unigram[i+1]) )
            tweets.append(tweet)
        count = count +1
    return tweets


def tweet_term (tweets) :
    """
        Generate tweet x term matrix
        # Input : list of tokenized tweets (uni or bi-gram)
        # Output : csr sparse matrix
    """    

    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    for value in tweets:
        for term in value :
            index = vocabulary.setdefault(term, len(vocabulary))
            indices.append(index)
            data.append(1)
        indptr.append(len(indices))
    
    return csr_matrix((data, indices, indptr), dtype=int)


def tweet_term_df (tweets):
    """
        Generate tweet x term matrix
        # Input : list of tokenized tweets (uni or bi-gram)
        # Output : dataframe
    """    
    
    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    for value in tweets:
        for term in value :
            index = vocabulary.setdefault(term, len(vocabulary))
            indices.append(index)
            data.append(1)
        indptr.append(len(indices))
    
    csr = csr_matrix((data, indices, indptr), dtype=int)

    csr_array = csr.toarray()
    sorted_voca = sorted(vocabulary.items(), key=itemgetter(1))
    new_voca=[]
    for i in sorted_voca:
        new_voca.append(i[0])
        
    return pd.DataFrame(csr_array, columns=new_voca)
    

def unigram_matrix (path):
    unigram = tokenize_unigram(path)
    return tweet_term_df(unigram)

def bigram_matrix (path):
    bigram = tokenize_bigram(path)
    return tweet_term_df(bigram)
    

if __name__ == "__main__":
    
    path = '/home/mira/Who-Wins/dataset/dataset_complet.csv'
    
    uni = unigram_matrix (path)
    bi = bigram_matrix (path)
    print(uni)
    print(bi)
    
    
    
    
    
    
    
    
    
    
