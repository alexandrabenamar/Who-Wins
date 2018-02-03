#!/usr/bin/python
#-*- coding: utf-8 -*-
from tweet import Tweet

class TweetLabour(Tweet):
    """ Classe définissant un Tweet mentionnant le parti Labour
        ayant pour candidat Ed Miliband """

    def __init__(self, id, username, nbrRT, text, hashtags, date, mentions):
        Tweet.__init__(self, id, username, nbrRT, text, hashtags, date, mentions)


if __name__ == "__main__":
    tweet = TweetLabour(234, "username", 1, "There's still hope, keep voting !!! #Labour #Miliband2015", ["#Labour", "#Miliband2015"], "18/03/2015", None)
    print(tweet.__dict__)
