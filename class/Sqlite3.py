#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3
conn = sqlite3.connect('../sqlite3/database.db')

c = conn.cursor()

c.execute("select * from collaborateur")
for row in c:
    print row


conn.close()