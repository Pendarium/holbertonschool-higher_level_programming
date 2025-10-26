#!/usr/bin/python3
"""
This module contains a script that does a data
request to database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # function to connect to a MySQL database
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password,
        db=database, port=3306
    )
    cur = db.cursor()
    # créer un curseur - permet d'avoir plusieurs environnement
    # sur la même connexion à la DB ?

    cur.execute(
        "SELECT c.name FROM cities AS c "
        "LEFT JOIN states AS s ON s.id = c.state_id "
        "WHERE s.name LIKE BINARY %s", (state,))
    # envoie une requête
    rows = cur.fetchall()
    # récupère les lignes renvoyées par la base
    # et les stock en liste de tuples
    # on peut récupérer une ligne à la fois ou un nombre n de lignes
    # avec fetchone() et fetchmany(n)

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()
