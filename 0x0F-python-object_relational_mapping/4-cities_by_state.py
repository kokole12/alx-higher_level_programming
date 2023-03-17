#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
            host='localhost', user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    command = cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)

