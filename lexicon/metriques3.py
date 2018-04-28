import pandas as pd
import numpy as np
import sys
import csv
from lexicon_weights import weight_positive_negative
from textblob import TextBlob
import polyglot
from polyglot.text import Text
import time

"""
Les données nettoyées doivent etre de la forme
id_tweet;post_tweet
id_tweet;post_tweet
id_tweet;post_tweet

"""

DIC_WORDS="senticnet4.txt"

def calcul_metriques(data):

	############
	#### Termes positifs et négatifs
	############
	print("Lecture positifs / negatifs")
	negative=[]
	positive=[]
	dict_test=open(DIC_WORDS, "r")
	for line in dict_test:
		mot,signe,poids=line.split("\t")
		if(signe=="positive"):
			positive.append(mot)
		else:
			negative.append(mot)

	############
	#### Récupération des tweets dans un dictionnaire
	############
	print("Lecture Tweets...")
	reader = csv.reader(open(data, 'r'),delimiter=';')
	tweet_dict = {}
	for key,value in reader:
		tweet_dict[key] = value

	############
	#### Récupération des tweets dans un dictionnaire
	############
	print("Calculs de métriques...")

	cpt = 0
	data_f=pd.DataFrame(np.zeros((len(tweet_dict.keys()),8)),columns=["pos","neg","none","nb_words","-neg+posM0","weight_n_posM1","weight_n_posM2","weight_n_posM3"],index=tweet_dict.keys())
	for key,value in tweet_dict.items():
		cpt+=1
		print(str(cpt) + " : " + key+"\n")

		pos=0
		neg=0
		nb_w=0
		texte=value.split()

		####
		# Methode 0
		# using pos / negs
		####
		for elem in texte:
			nb_w+=1
			if elem in positive:
				data_f.at[key,"pos"]+=1
			elif elem in negative:
				data_f.at[key,"neg"]+=1
			else:
				data_f.at[key,"none"]+=1

		data_f.at[key,"nb_words"]=nb_w

		data_f.at[key,"-neg+posM0"]=data_f.at[key,"pos"]-data_f.at[key,"neg"]

		####
		# Methode 1
		# using lexicon
		####
		data_f.at[key,"weight_n_posM1"]=weight_positive_negative(texte)

		####
		# Methode 2
		# using textblob
		####
		sentence=TextBlob(value)
		data_f.at[key,"weight_n_posM2"]=sentence.sentiment.polarity

	data_f.to_csv(path_or_buf="data.sentiment.output3.csv",sep=';',columns=["pos","neg","none","nb_words","-neg+posM0","weight_n_posM1","weight_n_posM2","weight_n_posM3"],header=True,index =True,index_label="id_tweet",mode='w')
	#print(data_f)
	print("\nSee "+"data.sentiment.output3.csv")



if __name__ == '__main__':

	if (len(sys.argv)) == 2 :
		f=open("time3.txt","w")
		start = time.time()
		calcul_metriques(sys.argv[1])
		f.write("time2: "+str(time.time()-start)+"s")

	else:
		print("\nIl faut en argument le nom d'un fichier !")
