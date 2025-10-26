#!/usr/bin/python3
"""
Liste toutes les villes de la base de données hbtn_0e_4_usa.
Usage :
    ./script.py <mysql_user> <mysql_password> <database>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cur = db.cursor()
    # Récupérer toutes les villes triées par id
    cur.execute("SELECT name FROM cities ORDER BY id ASC")
    rows = cur.fetchall()

    # Affichage sous forme de ligne séparée par des virgules
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()
