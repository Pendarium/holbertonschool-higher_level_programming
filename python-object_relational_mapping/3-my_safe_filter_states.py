#!/usr/bin/python3
"""
Affiche toutes les lignes de la table states dont le nom correspond
exactement à l'argument passé (sécurisé contre les injections).
Usage: ./script.py <mysql_user> <mysql_password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_arg = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (name_arg,)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
