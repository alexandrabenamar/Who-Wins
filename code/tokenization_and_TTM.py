#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk import word_tokenize
from scipy.sparse import csr_matrix
from operator import itemgetter
import pandas as pd


def tokenize_unigram (tweets):
    """
        Generate uni-gram tokenization
        # Input : list of cleansed tweet texts
        # Output : list of tokenized tweets
    """

    tweets_tok = []
    
    for tw in tweets:
        tweets_tok.append(word_tokenize(tw))
    
    return tweets_tok
    

def tokenize_bigram (tweets):
    """
        Generate bi-gram tokenization
        # Input : list of cleansed tweet texts
        # Output : list of bi-gram tokenized tweets
    """
    
    tweets_tok = []
    
    for tw in tweets:
        unigram = word_tokenize(tw)
        tweet = []
        for i in range(len(unigram)-1) :
            tweet.append( (unigram[i],unigram[i+1]) )
        tweets_tok.append(tweet)
    
    return tweets_tok


def tweet_term (tweets_tok) :
    """
        Generate tweet x term matrix
        # Input : list of tokenized tweets (uni or bi-gram)
        # Output : csr sparse matrix
    """    

    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    for value in tweets_tok:
        for term in value :
            index = vocabulary.setdefault(term, len(vocabulary))
            indices.append(index)
            data.append(1)
        indptr.append(len(indices))
    
    return csr_matrix((data, indices, indptr), dtype=int)


def tweet_term_df (tweets_tok):
    """
        Generate tweet x term matrix
        # Input : list of tokenized tweets (uni or bi-gram)
        # Output : dataframe
    """    
    
    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    for value in tweets_tok:
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
   
    
def unigram_matrix (tweets):
    """
        Generate csr version of the tweet x term matrix (unigram)
        # Input : list of cleansed tweet texts
        # Output : sparce matrix
    """ 
    unigram = tokenize_unigram(tweets)
    return tweet_term(unigram)


def bigram_matrix (tweets):
    """
        Generate csr version of the tweet x term matrix (bigram)
        # Input : list of cleansed tweet texts
        # Output : sparse matrix
    """
    bigram = tokenize_bigram(tweets)
    return tweet_term(bigram)


def unigram_matrix_df (tweets):
    """
        Generate dataframe version of the tweet x term matrix (unigram)
        # Input : list of cleansed tweet texts
        # Output : dataframe
    """ 
    unigram = tokenize_unigram(tweets)
    return tweet_term_df(unigram)


def bigram_matrix_df (tweets):
    """
        Generate dataframe version of the tweet x term matrix (bigram)
        # Input : list of cleansed tweet texts
        # Output : dataframe
    """
    bigram = tokenize_bigram(tweets)
    return tweet_term_df(bigram)



if __name__ == "__main__":
    
    tweets = [ "je suis une phrase" , "I am a sentence" , "I suis a phrase merci a toi" ]
    
    uni = unigram_matrix_df (tweets)
    bi = bigram_matrix_df (tweets)
    print(uni)
    print(bi)
    
    
    
    
    
    
    
    
    
    
