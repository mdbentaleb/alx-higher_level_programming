#!/usr/bin/python3
"""
Lists all cities from the database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    [print(city) for city in c.fetchall()]
