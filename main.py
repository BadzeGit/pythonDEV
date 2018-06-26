#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('class')
from Collaborateur import *



h1 = Collaborateur("Billiard","Fabien","Hotliner","fabien.billiard@itga.fr","0223440735","Super Cool ce mec", "ITGA", "Boite cool")



h1.voirCollaborateur()

h1.informationEntrep = "ZOB"

h1.voirCollaborateur()

"""
h2 = Entreprise("ZOBTEAM","balbla")
print(h2.raisonSociale)
h2.raisonSociale = "aaa"
print(h2.raisonSociale)"""