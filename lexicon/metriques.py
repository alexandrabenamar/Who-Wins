import sys
import csv
from lexicon_weights import weight_positive_negative
from textblob import TextBlob
import time

"""
Les données nettoyées doivent etre de la forme
id_tweet;post_tweet
id_tweet;post_tweet
id_tweet;post_tweet

"""

DIC_WORDS="senticnet4.txt"

def calcul_metriques(inital_file, file_to_csv):

	output = open(file_to_csv, 'a')
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
	#### Récupération des tweets dans un dictionnaire et calcul de métriques
	############
	print("Lecture Tweets... et calcul de métriques")

	reader = csv.reader(open(inital_file, 'r'),delimiter=';')
	tweet_dict = {}

	cpt = 0
	for key,value in reader:

		#Ou sommes nous ?
		cpt+=1
		print(str(cpt) + " : " + key+"\n")

		# Préparation pour calcul de métriques
		pos=0
		neg=0
		none=0
		nb_w=0
		texte=value.split()

		for elem in texte:
			nb_w+=1
			if elem in positive:
				pos+=1
			elif elem in negative:
				neg+=1
			else:
				none+=1

		result_m1 = pos-neg

		result_m2 = weight_positive_negative(texte)

		sentence=TextBlob(value)
		result_m3 = sentence.sentiment.polarity

		output.write(str(key) + "|" + value + "|" + str(pos) + "|" +  str(neg) + "|" +  str(none) + "|" +  str(result_m1) + "|" +  str(result_m2) + "|" +  str(result_m3) + "\n")

	output.close()

def to_csv(to_csv,csv_f):

	with open(to_csv, "r") as in_text:
	    in_reader = csv.reader(in_text, delimiter = '|')
	    with open(csv_f, "w") as out_csv:
	        out_writer = csv.writer(out_csv, lineterminator='\n', dialect='excel', delimiter=';')
	        for row in in_reader:
	            out_writer.writerow(row)

if __name__ == '__main__':

	if (len(sys.argv)) == 2 :
		if(sys.argv[1] == "output1.clean.csv"):
			TIME_F = "time1.txt"
			TO_CSV_F = "results1.txt"
			CSV_F = "output_end.csv"

		elif(sys.argv[1] == "output2.clean.csv"):
			TIME_F = "time1.txt"
			TO_CSV_F = "results1.txt"
			CSV_F = "output_end.csv"
		else:
			print("IF TIME.TXT AND RESULTS.TXT ALREADY EXIST : oldest data overwritten ")
			TIME_F = "time.txt"
			TO_CSV_F = "results.txt"
			CSV_F = "output_end.csv"

		f=open(TIME_F,"w")
		start = time.time()
		#calcul_metriques(sys.argv[1], TO_CSV_F)
		to_csv(TO_CSV_F, CSV_F)
		f.write("time1: "+str(time.time()-start)+"s")

	else:
		print("\nIl faut en argument le nom d'un fichier !")
