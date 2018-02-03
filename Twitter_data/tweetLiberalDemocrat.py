#!/usr/bin/python
#-*- coding: utf-8 -*-
from tweet import Tweet

class TweetLiberalDemocrat(Tweet):
    """ Classe définissant un Tweet mentionnant le parti Liberal
        Democrat ayant pour candidat Nick Clegg """

    def __init__(self, id, username, nbrRT, text, hashtags, date, mentions):
        Tweet.__init__(self, id, username, nbrRT, text, hashtags, date, mentions)


if __name__ == "__main__":
    tweet = TweetLiberalDemocrat(83, "username", 92, "There's no way the liberals will win", ["#Clegg"], "18/03/2015", None)
    print(tweet.__dict__)
