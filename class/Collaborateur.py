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

####################################

	@property	
	def nom(self):
		return self.__nom
	
	@nom.setter
	def nom(self, v):
		self.__nom = v


	@property
	def prenom(self):
		return self.__prenom

	@prenom.setter
	def prenom(self, v):
		self.__prenom = v


	@property
	def poste(self):
		return self.__poste

	@poste.setter
	def poste(self, v):
		self.__poste = v


	@property
	def mail(self):
		return self.__mail

	@mail.setter
	def mail(self, v):
		self.__mail = v


	@property
	def telephone(self):
		return self.__telephone

	@telephone.setter
	def telephone(self, v):
		self.__telephone = v


	@property
	def informationCollab(self):
		return self.__informationCollab

	@informationCollab.setter
	def informationCollab(self, v):
		self.__informationCollab = v


#####################################################


	def voirCollaborateur(self):
		print("Nom : {}\nPrénom : {}\nPoste : {}\nMail : {}\nTéléphone : {}\nInformations Collaborateur : {}\nRaison Sociale : {}\nInformation Entreprise : {}".format(self.nom, self.prenom, self.poste, self.mail, self.telephone, self.informationCollab, self.raisonSociale, self.informationEntrep))


