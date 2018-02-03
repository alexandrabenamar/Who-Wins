#!/usr/bin/python
#-*- coding: utf-8 -*-
from tweet import Tweet

class TweetConservative(Tweet):
    """ Classe définissant un Tweet mentionnant le
        parti conservateur ayant pour candidat David Cameron """

    def __init__(self, id, username, nbrRT, text, hashtags, date, mentions):
        Tweet.__init__(self, id, username, nbrRT, text, hashtags, date, mentions)


if __name__ == "__main__":
    tweet = TweetConservative(10, "username", 9, "@Cameron is going to win ! #Conservative #Cameron2015", ["#Conservative", "#Cameron2015"], "21/03/2015", "@Cameron")
    print tweet.__dict__
