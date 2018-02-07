#!/usr/bin/python
#-*- coding: utf-8 -*-
from tweet import *
import csv

class pars_csv:
    """ Classe permettant de parser un fichier csv afin de
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
        with open(self.pathway) as f_obj:
            reader = csv.DictReader(f_obj, delimiter=';')
            for line in reader:
                username=line['username']
                text=line['text']
                hashtags=line['hashtags']
                retweets=line['retweets']
                favorites=line['favorites']
                date=line['date']
                mentions=line['mentions']
                geo=line['geo']
                new_tweet=Tweet(compteur, username, int(retweets)+int(favorites), text, hashtags, date, mentions)
                compteur+=1
                self.tweet_list.append(new_tweet)

        return self.tweet_list

if __name__ == "__main__":
    csv_file = pars_csv("/Users/alexandrabenamar/Who-Wins/dataset/dataset_nettoye.csv")
    new_list = csv_file.parsFile()
    for tweet in new_list:
        print tweet.__dict__
