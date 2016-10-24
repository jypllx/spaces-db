#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import random
import math

def getRandomItem(cur, count):

    idx = math.floor(random.gauss(count/2,2))
    #print("ii %s" % (idx))
    if idx < 0 or idx >= count:
        return 0
    cur.execute("SELECT * FROM items ORDER BY id OFFSET %s LIMIT 1;", (idx,))
    item = cur.fetchone()
    return item 


def getRandomUser(cur):

    idx = random.randint(0,4999)
    cur.execute("SELECT * FROM users ORDER BY id OFFSET %s LIMIT 1;", (idx,))
    user = cur.fetchone()
    return user

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=spaces user=spaces")
    cur = conn.cursor()
    random.seed()

    cur.execute("SELECT count(*) FROM items;")
    count = cur.fetchone()[0]

    for i in range(0, 10000):

        item = getRandomItem(cur, count)
        user = getRandomUser(cur)
        # For now only complete plays are simulated

#        print("   "+str(item))
#        print("   "+str(user))
        if item == None or item == 0 or user == None:
            pass
        else :
            sql = "INSERT INTO plays (item_id, user_id) VALUES (%s, %s);"
            cur.execute(sql, (item[0], user[0]))
            conn.commit()

        print('%s' % (i))

    conn.close()


