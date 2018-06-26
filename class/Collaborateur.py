#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Entreprise import *

class Collaborateur(Entreprise):

	def __init__(self, nom, prenom, poste, mail, telephone, informationCollab, raisonSociale, informationEntrep):

		# Importation de la classe mère Entreprise
		Entreprise.__init__(self, raisonSociale, informationEntrep)

		print("Création du collaborateur")

		self.__nom = nom
		self.__prenom = prenom
		self.__poste = poste
		self.__mail = mail
		self.__telephone = telephone
		self.__informationCollab = informationCollab

	#######################################
	""" 	nom <getter><setter> 		"""
	#######################################

	def __getnom(self):
		print("Récupération de la valeur 'nom'")
		return self.__nom
	
	def __setnom(self, setNom):
		print("Modification de la valeur 'nom'")
		self.__nom = setNom

	nom = property(__getnom, __setnom)

	#######################################
	""" 	Prénom <getter><setter> 	"""
	#######################################

	def __getprenom(self):
		print("Récupération de la valeur 'prenom'")
		return self.__prenom

	def __setprenom(self, setprenom):
		print("Modification de la valeur 'prénom'")
		self.__prenom = setprenom

	prenom = property(__getprenom, __setprenom)

	#######################################
	""" 	Poste <getter><setter> 		"""
	#######################################

	def __getposte(self):
		print("Récupération de la valeur 'poste'")
		return self.__poste

	def __setposte(self, setposte):
		print("Modification de la valeur 'poste'")
		self.__poste = setposte

	poste = property(__getposte, __setposte)

	#######################################
	""" 	mail <getter><setter> 		"""
	#######################################

	def __getmail(self):
		print("Récupération de la valeur 'mail'")
		return self.__mail

	def __setmail(self, setmail):
		print("Modification de la valeur 'mail'")
		self.__mail = setmail

	mail = property(__getmail, __setmail)

	#######################################
	"""   telephone  <getter><setter> 	"""
	#######################################

	def __gettelephone(self):
		print("Récupération de la valeur 'telephone'")
		return self.__telephone

	def __settelephone(self, settelephone):
		print("Modification de la valeur 'telephone'")
		self.__telephone = settelephone

	telephone = property(__gettelephone, __settelephone)

	###############################################
	"""   informationCollab  <getter><setter> 	"""
	###############################################

	def __getinformationCollab(self):
		print("Récupération de la valeur 'informationCollab'")
		return self.__informationCollab

	def __setinformationCollab(self, setinformationCollab):
		print("Modification de la valeur 'informationCollab'")
		self.__informationCollab = setinformationCollab

	informationCollab = property(__getinformationCollab, __setinformationCollab)

	#################################################


	def voirCollaborateur(self):
		print("Nom : {}\nPrénom : {}\nPoste : {}\nMail : {}\nTéléphone : {}\nInformations Collaborateur : {}\nRaison Sociale : {}\nInformation Entreprise : {}".format(self.nom, self.prenom, self.poste, self.mail, self.telephone, self.informationCollab, self.raisonSociale, self.informationEntrep))


