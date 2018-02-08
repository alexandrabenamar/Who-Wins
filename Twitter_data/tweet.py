#!/usr/bin/python
#-*- coding: utf-8 -*-

class Tweet:
    """ Classe définissant un Tweet caractérisé par :
    - l'id de l'utilisateur
    - le nom de l'utilisateur (?) : problème d'anonymat
    - les mentions du Tweet
    - s'il s'agit ou non d'un RT
    - le texte du Tweet
    - les hashtags associés au Tweet """

    def __init__(self, id, username, nbrRT, text, hashtags, date, mentions):
        """ Constructeur de notre classe """
        self.id = id
        self.username = username
        self.mentions = mentions
        self.nbrRT = nbrRT
        self.text = text
        self.hashtags = hashtags
        self.date = date

    @property
    def id(self):
        """ getter identifiant"""
        return self.id

    @id.setter
    def id(self, uid):
        """ setter identifiant"""
        self.id = uid

    @property
    def username(self):
        """ getter nom de l'utilisateur """
        return self.username

    @username.setter
    def username(self, uname):
        """ setter nom de l'utilisateur """
        self.username = uname

    @property
    def mentions(self):
        """ getter mentions """
        return self.mentions

    @mentions.setter
    def mentions(self, mentions):
        """ setter nom de l'utilisateur"""
        self.mentions = mentions

    @property
    def nbrRT(self):
        """ getter nombre de retweets"""
        return self.nbrRT

    @nbrRT.setter
    def nbrRT(self, nbrRT):
        """ setter nombre de retweets"""
        self.nbrRT=nbrRT

    @property
    def date(self):
        """ getter date du tweet """
        return self.date

    @date.setter
    def date(self, d):
        """ setter nombre de retweets """
        self.date=d

if __name__ == "__main__":
    # test de creation d'un tweet
    tweet = Tweet(0, "username", 234, "@Obama Time to vote ! #vote", "#vote", "21/01/2015", "@Obama")
    print tweet.__dict__
