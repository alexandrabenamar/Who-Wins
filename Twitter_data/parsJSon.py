#!/usr/bin/python
#-*- coding: utf-8 -*-
from tweet import *

class ParsJSon:
    """ Classe permettant de parser un fichier json afin de
        récupérer tous les tweets contenus dedans"""

    def __init__(self, pathway):
        """ Constructeur de notre classe """
        self.pathway=pathway
        self.tweet_list=[]

    @property
    def pathway(self):
        return self.pathway

    @pathway.setter
    def pathway(self, pathway):
        self.pathway = pathway

    @property
    def tweet_list(self):
        return self.tweet_list

    @tweet_list.setter
    def tweet_list(self, tweet_list):
        self.tweet_list = tweet_list

    def parsFile(self):
        compteur=0
        name=""
        nbrRT=0
        text=""
        mentions=[]
        hashtags=[]
        date=""
        with open(self.pathway) as in_file:
            for line in in_file:
                if ("contributors" in line) and ("enabled" not in line):
                    compteur+=1

                if ("text" in line) and ("color" not in line):
                    if ("                " in line):
                        hashtags.append(line[25:][:len(line[25:])-2])
                    else:
                        text=line[13:][0:len(line[13:])-4]

                if ("screen_name" in line) and ("in_reply_to_screen_name" not in line) and ("                " in line):
                    mentions.append(line[32:][:len(line[32:])-2])

                if "retweet_count" in line:
                    nbrRT=line[21:][0:len(line[21:])-3]

                if ("created_at" in line) and ("        " not in line):
                    date=line[23:][0:len(line[23:])-4]

                if "location" in line:
                    location=line[21:][0:len(line[21:])-4]

                if ("name" in line) and (not "                " in line) and (not "screen" in line) and ("text" not in line):
                    name=line[17:][0:len(line[17:])-4]

                if ("verified" in line):
                    new_tweet=Tweet(compteur, name, nbrRT, text, hashtags, date, mentions)
                    self.tweet_list.append(new_tweet)
                    mentions[:] = []
                    hashtags[:] = []

        return self.tweet_list

if __name__ == "__main__":
    json = ParsJSon("/Users/alexandrabenamar/Who-wins/dataset/example.json")
    new_list = json.parsFile()
    for tweet in new_list:
        print tweet.__dict__
