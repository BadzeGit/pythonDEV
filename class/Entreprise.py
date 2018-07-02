#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entreprise(object):

	def __init__(self, raisonSociale, informationEntrep):
		self.__raisonSociale = raisonSociale
		self.__informationEntrep = informationEntrep


	@property
	def raisonSociale(self):
		return self.__raisonSociale

	@raisonSociale.setter
	def raisonSociale(self, v):
		self.__raisonSociale = v


	@property
	def informationEntrep(self):
		return self.__informationEntrep

	@informationEntrep.setter
	def informationEntrep(self, v):
		self.__informationEntrep = v


###############################################

