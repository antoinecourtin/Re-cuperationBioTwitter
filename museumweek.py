#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twython import Twython


APP_KEY = 'vosid'
APP_SECRET = 'vosid'
ACCESS_TOKEN = 'vosid'
ACCESS_TOKEN_SECRET = 'vosid'


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

    

