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

N_WORDS="negative-words.txt"
P_WORDS="positive-words.txt"
DIC_WORDS="senticnet4.txt"

def methode1(data):
	print ('ok')

def calcul_metriques(data):
	cpt=0
	negative=[]
	positive=[]

	print("Lecture positifs / negatifs")
	dict_test=open(DIC_WORDS, "r")
	for line in dict_test:
		mot,signe,poids=line.split("\t")
		if(signe=="positive"):
			positive.append(mot)
		else:
			negative.append(mot)

	#recupère les tweets dans un dictionnaire
	print("Lecture Tweets...")
	reader = csv.reader(open(data, 'r'),delimiter=';')
	tweet_dict = {}

	for key,value in reader:
		tweet_dict[key] = value

	print("Calculs")
	data_f=pd.DataFrame(np.zeros((len(tweet_dict.keys()),8)),columns=["pos","neg","none","nb_words","-neg+posM0","weight_n_posM1","weight_n_posM2","weight_n_posM3"],index=tweet_dict.keys())
	for key,value in tweet_dict.items():
		print(key+"\n")
		pos=0;neg=0

		texte=value.split()
		liste_p = []
		liste_n = []
		####
		# Methode 0
		####
		for elem in texte:
			if elem in positive:					
				data_f.at[key,"pos"]+=1
			elif elem in negative:
				data_f.at[key,"neg"]+=1
			else:
				data_f.at[key,"none"]+=1

		data_f.at[key,"nb_words"]=len(texte)

		data_f.at[key,"-neg+posM0"]=data_f.at[key,"pos"]-data_f.at[key,"neg"]
		#test
		if data_f.at[key,"pos"]-data_f.at[key,"neg"] >0:
			pos+=1
		elif data_f.at[key,"pos"]-data_f.at[key,"neg"]<0:
			neg+=1

		data_f.at[key,"weight_n_posM1"]=weight_positive_negative(texte)
		#test
		if weight_positive_negative(texte) >0:
			pos+=1
		elif weight_positive_negative(texte)<0:
			neg+=1

		####
		# Methode 2
		# using textblob
		####
		sentence=TextBlob(value)
		data_f.at[key,"weight_n_posM2"]=sentence.sentiment.polarity
		#test
		if sentence.sentiment.polarity >0:
			pos+=1
		elif sentence.sentiment.polarity<0:
			neg+=1


	data_f.to_csv(path_or_buf="data.sentiment.csv",sep=';',columns=["pos","neg","none","nb_words","-neg+posM0","weight_n_posM1","weight_n_posM2","weight_n_posM3"],header=True,index =True,index_label="id_tweet",mode='w')
	#print(data_f)
	print("\nSee "+"data.sentiment.csv")



if __name__ == '__main__':
	
	if (len(sys.argv)) == 2 :
		f=open("time1.txt","w")
		start = time.time()
		calcul_metriques(sys.argv[1])
		f.write("time1: "+str(time.time()-start)+"s")
		
	else:
		print("\nIl faut en argument le nom d'un fichier !")
