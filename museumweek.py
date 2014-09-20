#!/usr/bin/env python
# -*- coding: utf-8 -*-
# par antoine courtin
import warnings #pour pouvoir ensuite récupérer le message d'erreur de Twitter 
import time #pour pouvoir lancer la récupération en différé car l'API ne permet que 180 requêtes toutes les 15 minutes
from twython import Twython, TwythonError #les deux librairies issues de Twython

#Informations issues de Twitter sur le dev.center
APP_KEY = 'vosID'
APP_SECRET = 'vosID'
ACCESS_TOKEN = 'vosID'
ACCESS_TOKEN_SECRET = 'vosID'



# connexion à twitter pour récupérer les bios à partir de la liste d'utilisateurs figurant dans listecomptes.txt
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens(callback_url='votreURL')
comptes=open('listecomptes.txt','r')

# on met les comptes dans la liste listecomptes, en allant les lire à travers comptes (objet de type file)
listecomptes=[]
ligne=comptes.readline()

while ligne!='': 
	ligne=ligne.rstrip('\n\r') # pour avoir des strings listecomptes qui ne finissent pas par \n ou \r
	listecomptes.append(ligne)
	ligne=comptes.readline()
comptes.close()

#Véritables valeurs en fonction du nombre de compte de la liste 
nbTranches=47
tailleTranches=167 #RAPPEL: ne pas dépasser 180 
tempsAttente=910 #RAPPEL: ne pas aller en dessous de 900 secodnes (=15 minutes)

#valeurs pour les tests
#nbTranches=2
#tailleTranches=10
#tempsAttente=2

tranche=0 #on initialise les tranches
while tranche < nbTranches:
	#récupération des bios des comptes utilisateurs de la liste listecomptes ; on les met dans le fichier comptesbio.txt
	nomFichierBios='comptesbio'+str(tranche)+'.csv' #on créé autant de fichier CSV qu'il y a de tranches
	comptesbio=open(nomFichierBios, 'w')
	
	print ('Liste des comptes : ')
#	print listecomptes
#	listebios=[]
#	maxIdBio=75
#	print(tranche)
	max=tranche*tailleTranches
	idBio=max+1
#	print listecomptes[idBio]
		
	
	while idBio <=max+tailleTranches:   #len(listecomptes)-1:
		#Mise au point de la boucle
#		comptesbio.write(str(idBio))+';'+str(idBio+1)+';'+listecomptes[idBio]+'\n'
#		comptesbio.write(str(idBio)+'\n')		
		log=""
		try:user_timeline = twitter.show_user(screen_name=listecomptes[idBio])
		except TwythonError as e:
			print e
			log=str(e)
		description=user_timeline['description'] #la description équivaut dans Twitter aux biographies
		#print("***********\n"+" "+description+" : "+log)
		laBio=description
		#si le dernier caractère est \r, alors on remplace par '' : comme ça on n'ajoutera pas au fichier comptesBio les \r
		laBio=laBio.replace('\r', ', ')
		laBio=laBio.replace('\n', ', ')
		if log !="":#si le log n'est pas égal à rien = si il y a les 2 types de messages de warnings
			laBio=log	
		laBio=listecomptes[idBio]+';'+str(idBio)+';'+listecomptes[idBio]+';'+ laBio + '\n'
		comptesbio.write(laBio.encode("utf8"))
		idBio=idBio+1
	comptesbio.close()
	tranche=tranche+1	
	time.sleep(tempsAttente)
