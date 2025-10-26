#!/usr/bin/python3
"""
Affiche toutes les villes d'un état (nom passé en argument) à partir
de la base de données hbtn_0e_4_usa.

Usage:
    ./script.py <mysql_user> <mysql_password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cur = db.cursor()
    cur.execute(
        "SELECT c.name FROM cities AS c "
        "JOIN states AS s ON s.id = c.state_id "
        "WHERE s.name = %s "
        "ORDER BY c.id ASC",
        (state_name,)
    )

    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()
