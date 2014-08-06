#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twython import Twython


APP_KEY = 'JNRZRt7FthtCud17prlCEbgrg'
APP_SECRET = 'EQST5754eyzyPnFVcXdeR9vO6k3iScUaRHAxvgGElTdv23GHe3'
ACCESS_TOKEN = '119048849-Ev14VyT6yoS70q1IJgdc9aGW5nck7WV1WxEg8G52'
ACCESS_TOKEN_SECRET = '2HR2PDglEJo6KOkTYwvHIO7bPfW3ReRscDSnawXTV3eQg'


twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens(callback_url='http://museumweek.antoinecourtin.com/')
comptes=open('listecomptes.txt','r')
listecomptes=[]
ligne=comptes.readline()

while ligne!='': 
	listecomptes.append(ligne)
	ligne=comptes.readline()
comptes.close()
comptesbio=open('comptesbio.txt', 'w')

listesansretour=[]
for name in listecomptes:
	name = name.split('\n')[0]
	listesansretour.append(name)

print listesansretour

for username in listesansretour: # 
	try:
	    user_timeline = twitter.show_user(screen_name=username)
	except TwythonError as e:
		print e
	description=user_timeline['description']
	comptesbio.write(username+';'+ description.encode("utf8")+'\n')		
comptesbio.close()

    

