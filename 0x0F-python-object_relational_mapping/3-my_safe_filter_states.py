#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host='localhost', user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    command = cur.execute("SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    states = cur.fetchall()
    for state in states:
        print(state)

