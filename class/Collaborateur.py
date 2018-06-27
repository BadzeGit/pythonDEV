#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Entreprise import *

class Collaborateur(Entreprise):

	def __init__(self, nom, prenom, poste, mail, telephone, informationCollab, raisonSociale, informationEntrep):

		# Importation de la classe mère Entreprise
		Entreprise.__init__(self, raisonSociale, informationEntrep)

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
		return self.__nom
	
	def __setnom(self, setNom):
		self.__nom = setNom

	nom = property(__getnom, __setnom)

	#######################################
	""" 	Prénom <getter><setter> 	"""
	#######################################

	def __getprenom(self):
		return self.__prenom

	def __setprenom(self, setprenom):
		self.__prenom = setprenom

	prenom = property(__getprenom, __setprenom)

	#######################################
	""" 	Poste <getter><setter> 		"""
	#######################################

	def __getposte(self):
		return self.__poste

	def __setposte(self, setposte):
		self.__poste = setposte

	poste = property(__getposte, __setposte)

	#######################################
	""" 	mail <getter><setter> 		"""
	#######################################

	def __getmail(self):
		return self.__mail

	def __setmail(self, setmail):
		self.__mail = setmail

	mail = property(__getmail, __setmail)

	#######################################
	"""   telephone  <getter><setter> 	"""
	#######################################

	def __gettelephone(self):
		return self.__telephone

	def __settelephone(self, settelephone):
		self.__telephone = settelephone

	telephone = property(__gettelephone, __settelephone)

	###############################################
	"""   informationCollab  <getter><setter> 	"""
	###############################################

	def __getinformationCollab(self):
		return self.__informationCollab

	def __setinformationCollab(self, setinformationCollab):
		self.__informationCollab = setinformationCollab

	informationCollab = property(__getinformationCollab, __setinformationCollab)

	#################################################


	def voirCollaborateur(self):
		print("Nom : {}\nPrénom : {}\nPoste : {}\nMail : {}\nTéléphone : {}\nInformations Collaborateur : {}\nRaison Sociale : {}\nInformation Entreprise : {}".format(self.nom, self.prenom, self.poste, self.mail, self.telephone, self.informationCollab, self.raisonSociale, self.informationEntrep))


