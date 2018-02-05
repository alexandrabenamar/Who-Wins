#LIBRAIRIES UTILES
import tweepy
import json
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#AUTHENTIFICATION KEYS
access_token = "959197886314631168-W7zdSMzEucCG6RaSCeZqPl0YKPlLGJU"
access_token_secret = "wNYKAZtsZroAiD17anXAqpXj9QjB3eJtPj2YNyzvclGkP"
consumer_key = "UdQO7xkK2s2pgrjy5Vo1aqXkF"
consumer_secret = "Pe49stN74VDzRaIdCaTp9cYZY4AH5qcvAUxmFMpNVXLD8FSuyH"


#MAIN PROG
if __name__ == '__main__':

	#AUTHENTIFICATION
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	#api=tweepy.API(auth)

	#KEYWORDS FOR THE FILTER
	key_word = ["Conservative Party","The labour Party","The green party","LibDem","SNP"]
	key_word1 = ["GE2017","GE17"]
	key_word2 = ["Theresa May","Jeremy Corbyn","Caroline Lucas","Jonathan Bartley","Vince Cable","Nicola Sturgeon"]
	hashtags = ["Golden State"]
	
	query = "since:2017-06-01 until:2017-06-7  Conservative Party"
	
	#VARIABLES
	cpt = 0
	maxid= -1 # id tu tweet max
	sinceId =None #id du tweet min

	maxTweets=500
	tweetsPerQry=100

	while cpt < maxTweets:

		if maxid <=0:
			tweets =api.search(q=hashtags,count=tweetsPerQry,lang="en")
		else:
			tweets=api.search(q=hashtags,count=tweetsPerQry,lang="en",max_id=str(maxid -1))

		if tweets:
			for elements in tweets:
				print (elements.text)
			maxid=tweets[-1].id #curseur pour ne pas recuperer les mêmes tweets
			cpt +=len(tweets)
