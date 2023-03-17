#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    commad = cur.execute("SELECT cities.name FROM cities JOIN states ON \
            cities.state_id = states.id WHERE states.name = %(state)s \
            ORDER BY cities.id ASC", {'state': argv[4]})
    cities_in_state = cur.fetchall()
    for cities in cities_in_state:
        print(cities, end="")
    print()

