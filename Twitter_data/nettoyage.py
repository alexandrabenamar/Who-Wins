#!/usr/bin/python
#-*- coding: utf-8 -*-

def cleaning(sentence):
    """ Does different things :
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

    stopwords = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have",
    "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've",
    "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought",
    "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
    "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under",
    "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's",
    "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]

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
    for word in trash_words:                                        # removal of everything that was detected
        sentence=sentence.replace(word+" ","")

    sentence=sentence.strip()                                       # removal of spaces before and after
                                                                    # the sentence
    return sentence


if __name__ == "__main__":
    sentence="@ Mira RT: 1 the brexit will never ever pass or even be talked about, sorry guys, not gonna happen ! 3462892 http://www.google.fr # Brexit # Sortie2016"
    sentence=cleaning(sentence)
    print sentence
