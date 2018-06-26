#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entreprise(object):
	def __init__(self, raisonSociale, informationEntrep):
		print("Création de l' entreprise")
		self.raisonSociale = raisonSociale
		self.informationEntrep = informationEntrep

