import sys
import time

def classer(fichier):

	sortie=open("classification.txt","w")
	with open(fichier) as f:
		line=True
		while line:
			line=f.readline()
			tab=line.split("|")
			if(line):
				positive=0
				negative=0
				for i in range (5,8):
					if float(tab[i]) >0:
						positive+=1
					elif float(tab[i])<0:
						negative+=1
				if negative>positive:
					sortie.write(tab[0]+"|negative\n")
				elif positive >negative:
					sortie.write(tab[0]+"|positive\n")
				else:
					sortie.write(tab[0]+"|neutre\n")

	f.close()
	sortie.close()

if __name__ == '__main__':
	
	if (len(sys.argv)) == 2 :
		f=open("time.classification.txt","w")
		start = time.time()
		classer(sys.argv[1])
		f.write("time: "+str(time.time()-start)+"s")
		f.close()
		print("End")
	else:
		print("\nIl faut en argument le nom d'un fichier !")