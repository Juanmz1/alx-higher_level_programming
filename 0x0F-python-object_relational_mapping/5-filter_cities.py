#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM\
                cities JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cur.close()
    db.close()
