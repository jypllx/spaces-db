#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect("dbname=spaces user=spaces")
cur = conn.cursor();

for i in range(1, 5001):
    sql = "INSERT INTO users (firstname, lastname, login) VALUES (%s, %s, %s);"
    name = "user %s" % i
    cur.execute(sql, (name, name, name))
    conn.commit()
    print('inserted %s' % i)

cur.close()
conn.close()