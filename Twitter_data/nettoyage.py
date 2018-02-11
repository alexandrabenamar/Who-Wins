#!/usr/bin/python
#-*- coding: utf-8 -*-

import codecs

def cleaning(sentence):
    """ Data cleansing :
        # Removal of usernames (marked by @ symbol)
        # Removal of hashtags (marked by # symbol)
        # Removal of hyperlinks (URLs)
        # Removal of retweets symbol (marked by RT)
        # Removal of numbers
        # Removal of stop words using the stop word list on :
            https://github.com/Yoast/YoastSEO.js/blob/develop/src/config/stopwords.js
    """

    string=sentence

    spaces = string.count(" ")
    start = 0
    end = string.index(" ")
    trash_words = []
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    stopwords = codecs.open('/Users/alexandrabenamar/Who-Wins/dataset/stopwords.txt', mode='r').read().split('\n')

    flag=0
    for i in range(0, spaces+1):
        tmp_word = string[start:end]
        if ("@" in tmp_word) or ("#" in tmp_word):
            flag=1
            trash_words.append(tmp_word)                   # detection of "#" and "@" symbols
        elif flag == 1:                                      # detection of usernames and hashtags
            trash_words.append(tmp_word)
            flag = 0
        if ("RT" in tmp_word) or ("http" in tmp_word) or (".com/" in tmp_word):
            trash_words.append(tmp_word)                   # detection of hyperlinks and retweets symbols
        if (tmp_word in numbers):                          # detection of numbers
            trash_words.append(tmp_word)
        if (tmp_word in stopwords):                        # detection of stop words
            sentence=sentence.replace(tmp_word+" ", "")
        string=string[end+1:]
        if (string.count(" ") == 0):
            end=len(string)
        else:
            end=string.index(" ")

    sentence+=" "
    for word in trash_words:                               # removal of everything that was detected
        sentence=sentence.replace(word+" ","")

    sentence=sentence.strip()                              # removal of spaces before and after the sentence
    if not check_language(sentence):
        return None

    return sentence


def check_language(sentence):
    """
        Cheking if the language of the tweets is english
        Dictionnary : http://www.mit.edu/~ecprice/wordlist.10000
        Output :
            # true if the sentence is in english
            # false otherwise
    """
    eng_words = codecs.open('/Users/alexandrabenamar/Who-Wins/dataset/english_dictionnary.txt', mode='r').read().split('\n')

    words = toList(sentence)

    english_words = 0
    for word in words:
        if word in eng_words:
            english_words+=1

    return (english_words > 2)

def toList(sentence):
    """
        Transform a sentence into a list of words
            # Input : sentence to convert
            # Output : list of words
    """
    words = []
    tmp = []
    for char in sentence:
        if char == " ":
            words.append(tmp)
            tmp=""
        else:
            tmp += char
    if tmp:
        words.append(tmp)

    return words

if __name__ == "__main__":
    sentence="@ Mira RT: 1 the brexit will never ever pass or even be talked about, sorry guys, not gonna happen ! http://www.google.fr # Brexit # Sortie2016"
    sentence=cleaning(sentence)
    print sentence
    sentence = "je mange des frites"
    sentence=cleaning(sentence)
    print sentence
