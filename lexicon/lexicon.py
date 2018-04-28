import pandas as pd
import numpy as np
import sys
import csv
from lexicon_weights import weight_positive_negative

#recupere les fichiers
#dictionnaires +tweets
#save dico using utf-8
# a utiliser avec python3
"""
Les données nettoyées doivent etre de la forme
id_tweet;post_tweet
id_tweet;post_tweet
id_tweet;post_tweet

"""
DATA_CSV="data.csv"
N_WORDS="negative-words.txt"
P_WORDS="positive-words.txt"
DIC_WORDS="senticnet4.txt"

'''
Données retournées

occ_words:	Dataframe des occurences d'un mot  des dictionnaires dans un tweet 
occ_pos_neg:	DataFrame qui compte pour chaque tweets le nombre de mots positif et negatifs
data3:
'''

#Recuperer les dictionnaires dans des listes
def recherche(query,fichier="output_v2.csv"):
	cpt=0
	negative=[];positive=[];new_dico=[]

	"""
	with open(N_WORDS) as f:
		negative = f.read().splitlines()
	with open(P_WORDS) as f:
		positive = f.read().splitlines()
	with open(DIC_WORDS) as f:
		new_dico = f.read().splitlines()
	"""
	dict_test=open(DIC_WORDS, "r")
	for line in dict_test:
		mot,signe,poids=line.split("\t")
		if(signe=="positive"):
			positive.append(mot)
		else:
			negative.append(mot)

	#recupère les tweets dans un dictionnaire
	reader = csv.reader(open(DATA_CSV, 'r'),delimiter=';')
	tweet_dict = {}
	for key,value in reader:
		tweet_dict[key] = value

	if query == "occ_words":
		dico=negative+positive
		
		"""
		Creation d'un dataframe de la forme

					occ_mot1	occ_mot2	...
		idtweet-1		2 			1
		idtweet-2		0			3
			...
		"""

		col_test=["football", "teams","will","front","page","recession","VoteLeave","voters"]
		#utiliser COLUMN=dico pour les vrai données
		COLUMN=col_test

		data_f=pd.DataFrame(np.zeros((len(tweet_dict.keys()),len(COLUMN))),columns=COLUMN,index=tweet_dict.keys())

		#comptage occurences

		for key,value in tweet_dict.items():
			texte=value.split()
			for elem in texte:
				if elem in COLUMN:
					data_f.at[key,elem]+=1
		data_f.to_csv(path_or_buf=fichier,sep=';',columns=COLUMN,header=True,index =True,index_label=tweet_dict.keys(),mode='w')
		print("\n See {} ".format(fichier))
		print(data_f.head())
	elif query == "occ_pos_neg":
		"""
		Creation d'un dataframe de la forme

					positive	negative 	none	nb_words 	somme_neg_pos 		weight_p_n 
		idtweet-1		2 			0 		4		6
		idtweet-2		0			3		2 		5
			...
		"""
		data_f=pd.DataFrame(np.zeros((len(tweet_dict.keys()),6)),columns=["positive","negative","none","nb_words","somme_neg_pos","weight_p_n"],index=tweet_dict.keys())
		for key,value in tweet_dict.items():
			texte=value.split()
			liste_p = []
			liste_n = []
			for elem in texte:
				if elem in positive:
					if(key=="99999"):
						print("++ :",elem)
						#liste_p.append(elem)
					data_f.at[key,"positive"]+=1
				elif elem in negative:
					if(key=="99999"):
						print("-- :",elem)
						#liste_n.append(elem)
					data_f.at[key,"negative"]+=1
				else:
					data_f.at[key,"none"]+=1
			data_f.at[key,"nb_words"]=len(texte)
			data_f.at[key,"somme_neg_pos"]=data_f.at[key,"positive"]-data_f.at[key,"negative"]
			data_f.at[key,"weight_p_n"]=weight_positive_negative(texte)
			pos = ",".join(liste_p)
			neg = ",".join(liste_n)
			"""
			file = open("help.txt", 'x')
			file = open("help.txt", 'a')

			file.write("Pos : ")
			file.write(pos)
			file.write("Neg : ")
			file.write(neg)

			file.close()
			"""
		data_f.to_csv(path_or_buf=fichier,sep=';',columns=["nb_positive","nb_negative","nb_none","nb_words","somme_neg_pos","weight_p_n"],header=True,index =True,index_label="id_tweet",mode='w')
		print(data_f.head())
		print("\n See {} ".format(fichier))
	else:
		print("cette l'option n'existe pas !")


if __name__ == '__main__':
	print("1")
	if (len(sys.argv)) == 2 :
		print("a")
		recherche(sys.argv[1])
		print("b")
	elif (len(sys.argv)) == 3:
		print("c")
		recherche(sys.argv[1],sys.argv[2])
		print("d")
	else:
		print("e")
		print("\nAppel du script : python3 lexicon.py <option> <file:default=output_v$.csv>\nOption: occ_pos_neg, occ_words")
		print("f")

	print("2")