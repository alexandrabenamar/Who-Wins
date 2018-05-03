#!/usr/bin/python
#-*- coding: utf-8 -*-
import csv
import sys
from polyglot.detect import Detector
from polyglot.text import Text

def cleaning(sentence):
    """ Data cleansing using the stopwords list :
            https://github.com/Yoast/YoastSEO.js/blob/develop/src/config/stopwords.js
    """
    stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have",
    "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've",
    "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought",
    "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
    "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under",
    "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's",
    "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]

    kept = []
    for element in sentence.split(" "):
        if(element not in stopwords):
            kept.append(element)

    return " ".join(kept)

def anglais(obj):
    """
        Checking the english language of an object
    """
    for language in Detector(str(obj), quiet = True).languages:
        if(language.confidence > 60 and language.name == "anglais"):
            return obj
        else:
            return ""

def suppress(text):
    """
        Supressing :
            x punctuation
            x Twitter mentions (@)
            x Hashtags (#)
        
    """
    
    text=text.replace("\"", "")
    text=text.replace("/", "")
    text=text.replace("-", "")
    text=text.replace(",", "")
    text=text.replace(".", "")
    text=text.replace("!", "")
    text=text.replace("?", "")
    text=text.replace(":", "")
    text=text.replace(";", "")
    text=text.replace("\n", "")
    text=text.replace("@ ", "@")
    text=text.replace("# ", "#")

    return text

def clean(text):
    kept = []
    text = anglais(text)
    #print ("1 : anglais **" + text)
    text = cleaning(text)
    #print ("2 : cleaning **" + text)
    text = suppress(text)
    #print ("3 : suppress **" + text)
    for c in text.split(" "):
        #print("c : "+c +" t = " + str(len(c)))
        if (c.isalpha()):
            #print("alpha c : "+c)
            kept.append(c)
    text = ' '.join(kept)
    #print ("4 : clean ** " + text)
    return text

if __name__ == "__main__":
    if (len(sys.argv)) == 2 :

        reader = open(sys.argv[1], 'r', encoding='utf8')
        sortie=open("sortie.csv","w", encoding='utf8')
        
        L = []
        id=0

        for line in reader:
            print (id)
            line=''.join([x for x in line if x not in ["\x00", "\x01", "\x02", "\x03", "\x04", "\x05", "\x06", "\x07", "\x08", "\x0b", "\x0e", "\x0f", "\x10", "\x11", "\x12", "\x13", "\x14", "\x15", "\x16", "\x17", "\x18", "\x19", "\x1a", "\x1b", "\x1c", "\x1d", "\x1e", "\x1f", "\x7f", "\x80", "\x81", "\x82", "\x83", "\x84", "\x85", "\x86", "\x87", "\x88", "\x89", "\x8a", "\x8b", "\x8c", "\x8d", "\x8e", "\x8f", "\x90", "\x91", "\x92", "\x93", "\x94", "\x95", "\x96", "\x97", "\x98", "\x99", "\x9a", "\x9b", "\x9c", "\x9d", "\x9e", "\x9f"]])
            
            line=clean(line)
            #print("** " + line + " **")
            print(id)
            if(len(line) != 0):
                L.append(line)
                id+=1

        id = 0
        Q = list(set(L))
        for q in Q:
            print(id)
            sortie.write(str(id)+";"+q+"\n")
            id+=1

        print("\nSee sortie.csv")
       
        reader.close()
        sortie.close()
    else:
        print("\nIl faut en argument le nom d'un fichier !")
