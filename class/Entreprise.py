#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entreprise(object):

	def __init__(self, raisonSociale, informationEntrep):
		print("Création de l' entreprise")
		self.__raisonSociale = raisonSociale
		self.__informationEntrep = informationEntrep

	#######################################
	""" Raison Sociale <getter><setter> """
	#######################################

	def __getraisonSociale(self):
		print("Récupération de la valeur 'raisonSociale'") 
		return self.__raisonSociale


	def __setraisonSociale(self, setraisonSociale):
		print("Modification de la valeur 'raisonSociale'")
		self.__raisonSociale = setraisonSociale

	raisonSociale = property(__getraisonSociale,__setraisonSociale)

	##########################################
	""" informationEntrep <getter><setter> """
	##########################################

	def __getinformationEntrep(self):
		print("Récupération de la valeur 'informationEntrep'") 
		return self.__informationEntrep


	def __setinformationEntrep(self, setinformationEntrep):
		print("Modification de la valeur 'informationEntrep'")
		self.__informationEntrep = setinformationEntrep

	informationEntrep = property(__getinformationEntrep,__setinformationEntrep)

	##########################################