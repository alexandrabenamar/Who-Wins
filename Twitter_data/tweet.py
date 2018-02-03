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
        return self.id

    @id.setter
    def id(self, uid):
        self.id = uid

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, uname):
        self.username = uname

    @property
    def mentions(self):
        return self.mentions

    @mentions.setter
    def mentions(self, mentions):
        self.mentions = mentions

    @property
    def nbrRT(self):
        return self.nbrRT

    @nbrRT.setter
    def nbrRT(self, nbrRT):
        self.nbrRT=nbrRT

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, d):
        self.date=d

if __name__ == "__main__":
    tweet = Tweet(0, "username", 234, "@Obama Time to vote ! #vote", "#vote", "21/01/2015", "@Obama")
    print tweet.__dict__
