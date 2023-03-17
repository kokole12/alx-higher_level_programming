#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
            host='localhost', user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    commad = cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
    row = cur.fetchall()
    for state in row:
        print(state)

