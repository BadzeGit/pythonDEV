#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entreprise(object):

	def __init__(self, raisonSociale, informationEntrep):
		self.__raisonSociale = raisonSociale
		self.__informationEntrep = informationEntrep

	#######################################
	""" Raison Sociale <getter><setter> """
	#######################################

	def __getraisonSociale(self):
		return self.__raisonSociale


	def __setraisonSociale(self, setraisonSociale):
		self.__raisonSociale = setraisonSociale

	raisonSociale = property(__getraisonSociale,__setraisonSociale)

	##########################################
	""" informationEntrep <getter><setter> """
	##########################################

	def __getinformationEntrep(self):
		return self.__informationEntrep


	def __setinformationEntrep(self, setinformationEntrep):
		self.__informationEntrep = setinformationEntrep

	informationEntrep = property(__getinformationEntrep,__setinformationEntrep)

	##########################################