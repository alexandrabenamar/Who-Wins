# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:34:08 2018

@author: mira
"""


import re

#fonction pas encore terminée
#je suppose que le texte a été préalablement splité en "phrases" avec la 
#ponctuation comme séparateur. la liste de mots obtenue est donnée en paramètre.
#je suppose pour l'instant que tous les tokens sont positifs au départ. il faudra
#donc intégrer dans la fonction la recherche du mot dans le lexicon
#la fonction inverse donc la polarité des mots qui viennent après une négation
def negation (tokens):
    
    nb_tokens=len(tokens);
    pos_neg = []
    i=0
    
    while (i < nb_tokens):
        if tokens[i].lower() in ["no", "not", "anti"] or re.match(r"(.)*n't", tokens[i]):
            pos_neg.append(0)
            i = i+1
            if tokens[i].lower() in ["even", "really", "very", "exactly"]:
                pos_neg.append(0)
                i = i+1
                for j in range(i, nb_tokens):
                    pos_neg.append(-1)
                    i=i+1
            else:
                for j in range(i, nb_tokens):
                    pos_neg.append(1)
                    i=i+1
        else:
            pos_neg.append(1)        
            i=i+1
    
    return pos_neg

#test        
tokens = ["i" , "don't" , "really" , "agree" , "with" , "what" , "you" , "said" , "about" , "it"]
print(negation(tokens))



