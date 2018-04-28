# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 23:05:14 2018

@author: mira
"""



import pandas as pd


#fonction qui retourne la somme des poids selon le dico pondéré
def weight_positive_negative (sentence):
    df = pd.read_table("senticnet4.txt", header=None);
    
    lexicon = df.iloc[: , [0,2]]
    
    pos_neg=0
    
    for i in sentence:
        weight=lexicon.loc[(lexicon[0] == i)][2].tolist()
        if len(weight)>0:
            pos_neg=pos_neg + weight[0]
    return pos_neg

