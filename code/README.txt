#README

Quelques notes utiles pour l'algo d'extraction
A lancer avec python3

les librairies suivantes doivent etre installées
	tweepy
	json

lancer le script de la façon suivante:
	python3 data_extract.py > result.json
les resultats seront dans le fichier "result.json"
	
-------------
UK elections
-------------
	General election (tous les 5 ans)
		UK pop: 65 M
		Deux grands partis[Conservateurs,Labour Party]		

		Le parti ayant le plus de voix remporte l'éléction(326),son chef devient le 1er ministre
		La Reine nomme alors ou non ce premier ministre à la tête du gouvernement

		Derniere election: 8 Juin 2017(3 ans plus tôt)

		-------------------
		Les partis
		-------------------

		(1)Conservative Party:actual prime minister: Theresa May(Conservateurs)
		(2)The labour Party:Jeremy Corbyn
		(3)The green party :Caroline Lucas,Jonathan Bartley
		(4)LibDem:Vince Cable
		(5)SNP:Nicola Sturgeon

		(6)UKIP:Henry Borton
		(7)BNP:Adam Walker		
 
		-------------------
		A prendre en compte
		-------------------
		5 premiers partis
		lang=en
		du 1er au 7 Juin
		1 tweet 1 sujet
		geolocalisation:United Kingdom


	since:2013-08-05 until:2013-08-10 cats
	location
	geo
	As far as I know the API is limited to the last 7 days
