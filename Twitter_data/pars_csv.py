#!/usr/bin/python
#-*- coding: utf-8 -*-

from tweet import *
from nettoyage import *
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
        """ getter pathway """
        return self.pathway

    @pathway.setter
    def pathway(self, pathway):
        """ setter pathway """
        self.pathway = pathway

    @property
    def tweet_list(self):
        """ getter liste de tweets """
        return self.tweet_list

    @tweet_list.setter
    def tweet_list(self, tweet_list):
        """ setter liste de tweets """
        self.tweet_list = tweet_list

    def parsFile(self):

        with open(self.pathway) as f_obj:                   # ouverture du fichier csv
            reader = csv.DictReader(f_obj, delimiter=';')   # parser sous forme de dictionnaire le csv
            for line in reader:                             # récupération pour chaque tweets de toutes
                                                            # les informations contenues sur la ligne
                username=line['username']
                text=line['text']
                text=cleaning(text)
                hashtags=line['hashtags']
                retweets=line['retweets']
                favorites=line['favorites']
                date=line['date']
                mentions=line['mentions']
                geo=line['geo']
                # création de l'objet tweet : new_tweet
                new_tweet=Tweet(compteur, username, int(retweets)+int(favorites), text, hashtags, date, mentions)
                # ajout du tweet a la liste des tweets contenus dans le csv
                # uniquement si le tweet est en anglais
                if (text != None):
                    self.tweet_list.append(new_tweet)
        # retourner la liste des tweets contenus dans le csv
        return self.tweet_list

if __name__ == "__main__":
    # parser le fichier csv souhaite (le fichier doit avoir ete traite et nettoye au prealable)
    csv_file = pars_csv("/Users/alexandrabenamar/Who-Wins/dataset/dataset_complet.csv")
    new_list = csv_file.parsFile()      # recuperation de la liste de tweets
    for tweet in new_list:
        print tweet.__dict__            # affichage de la liste de tweets
