#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Entreprise import *

def formatString(value):
	v = value.capitalize()
	print(v)


class Collaborateur(Entreprise):
	def __init__(self, nom, prenom, poste, mail, telephone, informationCollab, raisonSociale, informationEntrep):

		Entreprise.__init__(self, raisonSociale, informationEntrep)
		
		print("Création du collaborateur")

		self.__nom = nom
		self.prenom = prenom
		self.poste = poste
		self.mail = mail
		self.telephone = telephone
		self.informationCollab = informationCollab


	def __getnom(self):
		print("Récupération non autorisé")
		return self.__nom
	
	def __setnom(self, setNom):
		print(len(setNom))
		if len(setNom) == 0: 
			print("chaine vide")



	



	nom = property(__getnom, __setnom)

	def voirCollaborateur(self):
		print("Nom : {}\nPrénom : {}\nPoste : {}\nMail : {}\nTéléphone : {}\nInformations Collaborateur : {}\nRaison sociale : {}\nInformations entreprise : {}".format(self.__nom, self.prenom, self.poste, self.mail, self.mail, self.informationCollab, self.raisonSociale, self.informationEntrep))





